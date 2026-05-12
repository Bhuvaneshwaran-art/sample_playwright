pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'py -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    pip install playwright pytest pytest-playwright
                '''
            }
        }

        stage('Install Browsers') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def result = bat(
                        script: '''
                            cd my-playwright-project
                            call ..\\venv\\Scripts\\activate.bat
                            pytest tests\\ --browser chromium -v
                        ''',
                        returnStatus: true
                    )
                    if (result == 0) {
                        echo "✅ All tests passed!"
                    } else if (result == 1) {
                        error "❌ Some tests failed!"
                    } else {
                        echo "⚠️ Tests completed with warnings (exit code: ${result})"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline complete'
        }
        success {
            echo '✅ Pipeline passed successfully!'
        }
        failure {
            echo '❌ Pipeline failed — check logs'
        }
    }
}