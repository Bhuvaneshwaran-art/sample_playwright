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
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pip install playwright pytest pytest-playwright
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Browsers') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest tests/ --browser chromium -v
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