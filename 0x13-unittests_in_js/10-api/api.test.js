const { expect } = require('chai');

const request = require('request');
const URL = 'http://localhost:7865/';
describe('cart endpoint', () => {
  it('endpoint Get /cart/:id<number>:', (done) => {
    const url = `${URL}cart/1`;
    request(url, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal(`Payment methods for cart 1`);
      done();
    });
  });
  it('endpoint Get /cart/:id<not number>:', (done) => {
    const url = `${URL}cart/k`;
    request(url, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

describe('/login endpoint', () => {
  it('Post /login', (end) => {
    const url = `${URL}login/`;
    const data = {
      method: 'POST',
      url,
      json: true,
      body: { userName: 'Test' },
    };
    request(data, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Test');
      end();
    });
  });
  it('Post /login/Something to be status code 404', (end) => {
    const url = `${URL}login/something`;
    const data = {
      method: 'POST',
      url,
      json: true,
      body: { userName: 'Test' },
    };
    request(data, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      end();
    });
  });
});

describe('/available_payments endpoint', () => {
  it('Get /available_payments should return {payment_methods: {credit_cards: true, paypal: false,},}', () => {
    const url = `${URL}available_payments/`;
    request(url, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal(
        '{"payment_methods":{"credit_cards":true,"paypal":false}}'
      );
    });
  });
});
