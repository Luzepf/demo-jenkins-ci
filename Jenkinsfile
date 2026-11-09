pipeline {
    agent any

    stages {
        stage('Verificar entorno') {
            steps {
                bat 'python --version'
                bat 'python -m pytest --version'
            }
        }
        stage('Ejecutar tests') {
            steps {
                bat 'python -m pytest -v --junitxml=resultados.xml'
            }
        }
    }

    post {
        always {
            junit 'resultados.xml'
        }
        success {
            echo 'Todos los tests pasaron. Integración exitosa.'
        }
        failure {
            echo 'Hay tests fallando. Revisar antes de integrar.'
        }
    }
}
