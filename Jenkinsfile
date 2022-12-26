pipeline {
    agent any

    stages {
        stage('Chcekcout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'firstpole_git', url: 'https://github.com/firstPole/front-end.git']]])
            }
        }
      stage('Detect Secret') {
              steps {
                  withCredentials([string(credentialsId: 'GITGUARDIAN_API_KEY', variable: 'GITGUARDIAN_API_KEY')]) {
                    sh 'ggshield secret scan --json path . --recursive -y | sudo tee -a sensitive-report.json'
                   // sh 'ggshield secret scan --json path . --recursive -y'
                  }
        }
    }
    }
}
