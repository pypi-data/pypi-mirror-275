package lib

import (
	"os"
	"path/filepath"
)

func writeLib(libDir, libFullName string, content []byte, versionMatched bool) error {
	libFullPath := filepath.Join(libDir, libFullName)
	_, err := os.Stat(libFullPath)
	if os.IsNotExist(err) || !versionMatched {
		err = os.MkdirAll(libDir, 0777)
		if err != nil {
			return err
		}
		libFile, err := os.Create(libFullPath)
		defer func() {
			libFile.Close()
		}()
		if err != nil {
			return err
		}
		_, err = libFile.Write(content)
		if err != nil {
			return err
		}
	}
	return err
}
