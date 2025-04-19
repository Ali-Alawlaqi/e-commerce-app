pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '. venv/bin/activate && sonar-scanner -Dsonar.projectKey=e-commerce-app -Dsonar.host.url=http://localhost:9000 -Dsonar.login=sqp_83b9d11937497899459e754613057bdc64dc292c'
                }
            }
        }
    }

    post {
        success {
            slackSend channel: '#devops', message: "✅ Build succeeded: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
        failure {
            slackSend channel: '#devops', message: "❌ Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}
