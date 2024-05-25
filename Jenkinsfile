pipeline {
    agent any

    environment {
        AWS_CREDENTIALS_ID = 'AWS_ACCESS_KEY_ID'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Terraform Init') {
            steps {
                sh 'pwd;cd terraform/ ; terraform init'
            }
        }
        
        stage('Terraform Apply') {
            steps {
                sh 'pwd;cd terraform/ ; terraform apply -auto-approve'
            }
        }

        // stage('Terraform Init') {
        //     steps {
        //         sh '/usr/local/bin/terraform init'
        //     }
        // }
        
        // stage('Terraform Apply') {
        //     steps {
        //         sh 'pwd; cd terraform/ ; pwd;  /usr/local/bin/terraform apply -auto-approve'
        //     //     withAWS(credentials: "${AWS_CREDENTIALS_ID}", region: 'us-east-1') {
        //     //         sh '/usr/local/bin/terraform apply -auto-approve'
        //     //     }
        //     }
        // }
        
        stage('Run Tests') {
            steps {
                withAWS(credentials: "${AWS_CREDENTIALS_ID}", region: 'us-east-1') {
                    sh 'pip install -r requirements.txt' // Ensure all dependencies are installed
                    sh 'behave'
                }
            }
        }

        stage('Terraform Destroy') {
            steps {
                withAWS(credentials: "${AWS_CREDENTIALS_ID}", region: 'us-east-1') {
                    sh '/usr/local/bin/terraform destroy -auto-approve'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
