pipeline {
    agent any

    environment {
        DOCKER_APP = "worldofgames-web"
        DOCKER_IMAGE = """orkilim/${DOCKER_APP}"""
        DOCKER_TAG = "latest"
        DOCKER_PORT = "8777"
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out the repository
                //git branch: 'master', url: 'https://github.com/orkilim/devops_final_project.git'
                bat 'if exist devops_final_project (rmdir /S /Q devops_final_project)'
                bat """git clone https://github.com/orkilim/devops_final_project.git"""
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    bat """docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."""
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the Docker container, expose port 8777, and mount dummy Scores.txt
                    bat """
                        echo "0" > dummy_scores.txt
                        docker-compose -f Docker-compose.yml up -d --build
                    """
                        //docker run -d -p ${DOCKER_PORT}:5000 --name worldofgames-test -v %cd%\\dummy_scores.txt:/Scores.txt ${DOCKER_IMAGE}:${DOCKER_TAG}
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    dir('devops_final_project') {
                    // Run Selenium tests using e2e.py (this should exist in your repo)
                    try {
                        bat 'cd tests && python e2e.py'
                    } catch (Exception e) {
                        error "Tests failed!"
                    }
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop the container
                    bat 'docker stop world-of-games-container && docker rm world-of-games-container'

                    // Ask the user for their DockerHub credentials and push the image
                    withCredentials([string(credentialsId: 'docker-hub-username', variable: 'DOCKER_HUB_USERNAME'),
                                     string(credentialsId: 'docker-hub-password', variable: 'DOCKER_HUB_PASSWORD')]) {

                        // Log in to DockerHub with the provided credentials
                        bat """docker login -u ${DOCKER_HUB_USERNAME} -p ${DOCKER_HUB_PASSWORD}"""

                        // Tag the image with the user's DockerHub username
                        bat """docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE}:${DOCKER_TAG}"""

                        // Push the image to the user's DockerHub account
                        bat """docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"""
                    }
                }
            }
        }
    }


}
