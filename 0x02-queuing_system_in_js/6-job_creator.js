var kue = require('kue');
var queue = kue.createQueue()

var jobData = {
  phoneNumber: 'string',
  message: 'string',
}

var push_notification_code = queue.create(jobData).save( function(err){
  console.log(`Notification job created: ${push_notification_code.id}`)
})

push_notification_code.on('complete', function(result){
  console.log('Notification job completed');
})

push_notification_code.on('failed', function(err){
  console.log('Notification job failed')
})
