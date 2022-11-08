var kue = require('kue');
var queue = kue.createQueue()

jobData = {
  phoneNumber: 'string',
  message: 'string',
}

push_notification_code = queue.create(jobData).save( function(err){
  console.log(`Notification job created: ${push_notification_code.id}`)
})

job.on('complete', function(result){
  console.log('Notification job completed');
})

job.on('failed', function(err){
  console.log('Notification job failed')
})
