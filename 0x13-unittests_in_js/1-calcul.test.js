const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber with type equal to SUM', function () {
  it('check that two numbers without float part are the expected sum', function () {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
    assert.equal(calculateNumber('SUM', 1, 8), 9);
    assert.equal(calculateNumber('SUM', 5, 7), 12);
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('check that the sum is working correctly with negative numbers', function () {
    assert.equal(calculateNumber('SUM', -5, 10), 5);
    assert.equal(calculateNumber('SUM', -6, -12), -18);
    assert.equal(calculateNumber('SUM', -999, -1), -1000);
    assert.equal(calculateNumber('SUM', 5, -10), -5);
  });
  it('The sum is executed correctly with a 0', function () {
    assert.equal(calculateNumber('SUM', 0, 5), 5);
    assert.equal(calculateNumber('SUM', 10, 0), 10);
    assert.equal(calculateNumber('SUM', 0, 0), 0);
    assert.equal(calculateNumber('SUM', -30, 0), -30);
  });
  it('Check in sum first number is integer number and second number is float number', function () {
    assert.equal(calculateNumber('SUM', 14, 0.7), 15);
    assert.equal(calculateNumber('SUM', 14, 0.4), 14);
  });
  it('Check in sum second number is integer number and first number is float number', function () {
    assert.equal(calculateNumber('SUM', 0.7, 14), 15);
    assert.equal(calculateNumber('SUM', 0.4, 14), 14);
  });
});

describe('calculateNumber with type equal to SUBTRACT', function () {
  it('check that two numbers without float part are the expected subtract', function () {
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.equal(calculateNumber('SUBTRACT', 1, 8), -7);
    assert.equal(calculateNumber('SUBTRACT', 5, 7), -2);
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.equal(calculateNumber('SUBTRACT', 3.1, 2.5), 0);
  });
  it('check that the subtract is working correctly with negative numbers', function () {
    assert.equal(calculateNumber('SUBTRACT', -5, 10), -15);
    assert.equal(calculateNumber('SUBTRACT', -6, -12), 6);
    assert.equal(calculateNumber('SUBTRACT', -999, -1), -998);
    assert.equal(calculateNumber('SUBTRACT', 5, -10), 15);
  });
  it('The subtract is executed correctly with a 0', function () {
    assert.equal(calculateNumber('SUBTRACT', 0, 5), -5);
    assert.equal(calculateNumber('SUBTRACT', 10, 0), 10);
    assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
    assert.equal(calculateNumber('SUBTRACT', -30, 0), -30);
  });
  it('Check first number is integer number and second number is float number', function () {
    assert.equal(calculateNumber('SUBTRACT', 14, 0.7), 13);
    assert.equal(calculateNumber('SUBTRACT', 14, 0.4), 14);
  });
  it('Check in subtract second number is integer number and first number is float number', function () {
    assert.equal(calculateNumber('SUBTRACT', 0.7, 14), -13);
    assert.equal(calculateNumber('SUBTRACT', 0.4, 14), -14);
  });
});

describe('calculateNumber with type equal to DIVIDE', function () {
  it('log an error when second number is 0', function () {
    assert.equal(calculateNumber('DIVIDE', 1, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -5, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -50.8, 0), 'Error');
  });
  it('log the expected result when second number is not 0', function () {
    assert.equal(calculateNumber('DIVIDE', 1, 3), 0.33);
    assert.equal(calculateNumber('DIVIDE', 1, 8), 0.13);
    assert.equal(calculateNumber('DIVIDE', 5, 7), 0.71);
    assert.equal(calculateNumber('DIVIDE', 5, 2), 2.5);
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.equal(calculateNumber('DIVIDE', 0, 4.5), 0);
  });
});

describe('calculateNumber with an incorrect type', function () {
  it('Expect to be undefined if type is not SUM, SUBTRACT or DIVIDE', function () {
    assert.equal(calculateNumber('DIV', 1, 3), undefined);
    assert.equal(calculateNumber('DIV', 1, 8), undefined);
    assert.equal(calculateNumber('DIV', 5, 7), undefined);
  });
});
