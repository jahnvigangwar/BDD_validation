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
                sh 'pwd;cd terraformFiles/ ; terraform init'
            }
        }

        stage('Terraform Validate') {
            steps {
                sh 'pwd;cd terraformFiles/ ; terraform validate'
            }
        }
        
        stage('Terraform Plan') {
            steps {
                sh 'pwd;cd terraformFiles/ ; terraform plan'
            }
        }
        
        stage('Terraform Apply') {
            steps {
                withAWS(credentials: "${AWS_CREDENTIALS_ID}", region: 'us-east-1') 
                {
                    sh 'pwd; cd terraformFiles/ ;  terraform apply -auto-approve'
                }
            }
        }
        
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
                    sh 'pwd; cd terraformFiles/; terraform destroy -auto-approve'
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
