pipeline{
    agent none
     

    environment{
            TEST="test value1"
            TEST1="test value 2"
              }
    parameters{
             string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
             text(name: 'BIOGRAPHY', defaultValue: 'krishna', description: 'Enter some information about the person')
              }
    stages{
        stage('Build'){
            agent {
                   label "slave1"
                   }
            steps{ 
                    sh ''' sleep 5
                    echo "$TEST" 
                '''
            }
            }

        stage('test'){
            agent any

            steps{
                 
                       echo "${params.PERSON}"
                       echo "${params.BIOGRAPHY}"
                       
            }
           
            }
        }
    }

