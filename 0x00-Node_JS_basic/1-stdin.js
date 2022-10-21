// takes info from user and displays
const readline = require('readline');

function nameIs() {
  const rl = readline.createInterface(
    process.stdin, process.stdout,
  );

  console.log(process.execArgv)
  if (Boolean(process.stdin.isTTY)){
    ques = 'Welcome to Holberton School, what is your name?\n'
  }
  else {
    ques = 'Welcome to Holberton School, what is your name?'
  }
  rl.question(ques, (name) => {
    console.log(`Your name is: ${name}`);
    console.log('This important software is now closing');
    rl.close();
  });
}
nameIs();
