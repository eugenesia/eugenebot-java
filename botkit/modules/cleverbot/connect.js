// Connect to the Cleverbot server
const net = require('net')
const port = 10000
const host = 'localhost'

const client = new net.Socket();
client.setEncoding('utf-8');

client.connect(port, host, () => {
	console.log('Connected');
	// client.write('Hello, server! Love, Client.\n');
});

/*
client.on('data', function(data) {
	console.log('Received: ' + data);
	client.destroy(); // kill client after server's response
});
*/

client.on('close', function() {
	console.log('Connection closed');
});

async function send(msg) {
	console.log('Message received', msg)
	client.write(msg + '\n');
	return new Promise((resolve, reject) => {

		client.on('data', data => {
			resolve(data);
		})

		client.on('error', error => {
			reject(error);
		})
	})
}

module.exports = {
	send
}
