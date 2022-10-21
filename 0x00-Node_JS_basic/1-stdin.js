// takes info from user and displays
const readline = require('readline');

function nameIs() {
  const rl = readline.createInterface(
    process.stdin, process.stdout,
  );

  console.log(process.argv);

  rl.question('Welcome to Holberton School, what is your name?', (name) => {
    console.log(`Your name is: ${name}`);
    console.log('This important software is now closing');
    rl.close();
  });
}
nameIs();
