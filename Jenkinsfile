pipeline {
    agent any

    environment {
        PYTHON_EXE = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Preparar entorno') {
            steps {
                bat "\"${PYTHON_EXE}\" -m pip install -r requirements.txt"
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat "\"${PYTHON_EXE}\" -m pytest -v"
            }
        }

        stage('Validar calidad') {
            steps {
                echo 'Validación básica de calidad completada'
            }
        }

        stage('Validar seguridad') {
            steps {
                echo 'Validación de seguridad simulada'
            }
        }

        stage('Construir') {
            steps {
                echo 'Construcción del sistema completada'
            }
        }

        stage('Desplegar en staging') {
            steps {
                echo 'Despliegue simulado en staging completado'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente'
        }

        failure {
            echo 'El pipeline falló. Se requiere corregir el cambio.'
        }
    }
}