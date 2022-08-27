import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];
const getItemById = (id) =>
  listProducts.filter((product) => product.Id === id)[0];

const reserveStockById = (itemId, stock) => client.set(itemId, stock);
const getCurrentReservedStockById = async (itemId) => {
  const stockPromise = promisify(client.get).bind(client);
  return await stockPromise(itemId);
};

app.get('/', (req, res) => res.send('Index page'));
app.get('/list_products', (req, res) => res.json(listProducts));

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId),
    product = getItemById(itemId);

  if (!product) return res.json({ status: 'Product not found' });
  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) {
    if (product.stock <= 0)
      return res.json({ status: 'Not enough stock available', itemId });
    return reserveStockById(itemId, product.stock - 1);
  } else if (currentStock <= 0)
    return res.json({ status: 'Not enough stock available', itemId });
  else {
    reserveStockById(itemId, currentStock - 1);
    return res.json({ status: 'Reservation confirmed', itemId });
  }
});

app.get('/list_products/:itemId', async (req, res) => {
  let itemId = parseInt(req.params.itemId);

  const stock = await getCurrentReservedStockById(itemId);

  let product = getItemById(itemId);
  if (product) {
    if (stock !== null) {
      product = { ...product, stock };
    }
    return res.json(product);
  }
  return res.json({ status: 'Product not found' });
});

const PORT = 1245;
app.listen(PORT, () => console.log(`Running on port ${PORT}`));
