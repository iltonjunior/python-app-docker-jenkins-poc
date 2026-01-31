pipeline {
    agent any

    environment {
        APP_NAME   = "python-app-docker-jenkins-poc"
        IMAGE_NAME = "metrofor/python-app-docker-jenkins-poc"
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                  docker build \
                    -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                    -t ${IMAGE_NAME}:latest \
                    .
                """
            }
        }

        stage('Deploy (Docker Compose)') {
            steps {
                sh """
                  docker compose down || true
                  docker compose up -d
                """
            }
        }

        stage('Health Check') {
            steps {
                sh """
                  sleep 5
                  curl -f http://localhost:5000
                """
            }
        }
    }

    post {
        success {
            echo "✅ Deploy realizado com sucesso!"
        }
        failure {
            echo "❌ Falha no pipeline"
        }
        always {
            sh "docker image prune -f || true"
        }
    }
}
