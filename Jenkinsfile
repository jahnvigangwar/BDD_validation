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
                sh 'pwd'
                sh 'cd /Users/jahnvi/.jenkins/workspace/BDD_validation_Pipeline@script/829e7402c981cfb1ce9c896c28ca3f73197eb1da8fa92b20cd3ddec253da08cc/terraform'
                sh 'pwd'
                sh '/usr/local/bin/terraform init'
                
            }
        }
        
        stage('Terraform Apply') {
            steps {
                sh 'pwd'
                sh 'cd /Users/jahnvi/.jenkins/workspace/BDD_validation_Pipeline@script/829e7402c981cfb1ce9c896c28ca3f73197eb1da8fa92b20cd3ddec253da08cc/terraform'
                sh 'pwd'
                withAWS(credentials: "${AWS_CREDENTIALS_ID}", region: 'us-east-1') {
                    sh '/usr/local/bin/terraform apply -auto-approve'
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
