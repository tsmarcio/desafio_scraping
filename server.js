import { createServer } = from 'node:http'

const server = createServer((req, res) => {
  console.log('oi')
});

server.listen(3333, () => {
  console.log('Servidor rodando em http://localhost:3333');
});
