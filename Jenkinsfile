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
                    pip install -r requirements.txt
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
                bat '''
                    cd my-playwright-project
            pytest tests\\ --browser chromium -v
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline complete'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}