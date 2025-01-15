pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yuvalbenar/weathertraining-app"
        DOCKER_TAG = "${BRANCH_NAME}-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-creds', url: '']) {
                        sh """
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push ${DOCKER_IMAGE}:latest
                        """
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Update the Kubernetes deployment to use the new Docker image
                    sh """
                    kubectl set image deployment/weather-app weather-app=${DOCKER_IMAGE}:${DOCKER_TAG}
                    kubectl rollout status deployment/weather-app
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
        }
    }
}




// pipeline {
//     agent any

//     environment {
//         DOCKER_IMAGE = "yuvalbenar/weathertraining-app"
//         DOCKER_TAG = "${BUILD_NUMBER}"
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     sh """
//                     docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
//                     docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
//                     """
//                 }
//             }
//         }

//         stage('Push to Docker Hub') {
//             when {
//                 branch 'main'
//             }
//             steps {
//                 script {
//                     withDockerRegistry([credentialsId: 'docker-hub-creds', url: '']) {
//                         sh """
//                         docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
//                         docker push ${DOCKER_IMAGE}:latest
//                         """
//                     }
//                 }
//             }
//         }

//         stage('Create Merge Request') {
//             when {
//                 not {
//                     branch 'main'
//                 }
//             }
//             steps {
//                 echo "Trigger a manual merge request to the main branch!"
//             }
//         }
//     }
// }
