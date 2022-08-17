const { expect } = require('chai');

const request = require('request');

describe('Request to the root path', () => {
  it('endpoint Get /cart/:id<number>:', (done) => {
    const URL = 'http://localhost:7865/cart/1';
    request(URL, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal(`Payment methods for cart 1`);
      done();
    });
  });
  it('endpoint Get /cart/:id<not number>:', (done) => {
    const URL = 'http://localhost:7865/cart/k';
    request(URL, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
