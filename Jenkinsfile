pipeline{
    agent none
    stages{
        stage('Build'){
            agent {
                   label "slave1"
                   }
            steps{ 
                    sh ''' sleep 5
                    echo "========executing A========" 
                '''
            }
            }
        stage('test'){
            agent {
                   label "slave1"
                   }

             steps{
                   sh '''
                        sleep 5
                   echo "========executing A========" 
                '''
            }
           
            }
        }
    }

