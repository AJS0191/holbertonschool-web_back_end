const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

var kue = require('kue');
var queue = kue.createQueue();


  
jobs.forEach(job => {
    
    var push_notification_code2 = queue.create(job).save( function(err){
        console.log(`Notification job created: ${job.id}`)
      })
      
      push_notification_code2.on('complete', function(result){
        console.log(`Notification job ${job.id} completed`);
      })
      
      push_notification_code2.on('failed', function(err){
        console.log(`Notification job ${job.id} failed: ${err}`)
      })

      push_notification_code2.on('progress', function(progress, data){
        console.log(`Notification job ${job.id} ${progress} complete`)
      })
});