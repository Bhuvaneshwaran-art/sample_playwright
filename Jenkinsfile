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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install playwright pytest pytest-playwright
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Browsers') {
            steps {
                sh '''
                    . venv/bin/activate
                    playwright install chromium
                    playwright install-deps chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ --browser chromium -v
                '''
            }
        }
    }

    post {
        always {
            echo 'Done'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}