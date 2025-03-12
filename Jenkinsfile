pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/bc0de0/cyberpunk-security.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Security Checks') {
            steps {
                sh 'source venv/bin/activate && flake8 main.py'
            }
        }

        stage('Run Application') {
            steps {
                sh 'source venv/bin/activate && python main.py &'
            }
        }
    }
}