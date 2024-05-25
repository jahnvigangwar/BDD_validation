pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
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
                sh 'pwd; cd terraformFiles/ ;  terraform apply -auto-approve'
            }
        }
        
        stage('Run Tests') {
            steps {
                // sh 'pipx install -r requirements.txt' // Ensure all dependencies are installed
                sh 'pipx install behave'
                sh 'pip install boto3'
                sh 'pip install python-terraform'
                sh 'behave'
            }
        }

        stage('Terraform Destroy') {
            steps {
                sh 'pwd; cd terraformFiles/; terraform destroy -auto-approve'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
