pragma solidity ^0.8.0;

contract ProductTrace {
    struct Product {
        uint id;
        string name;
        string origin;
        string[] history;
    }

    mapping(uint => Product) private products;
    uint private productCount;

    event ProductAdded(uint id, string name, string origin);
    event ProductUpdated(uint id, string update);

    constructor() {
        productCount = 0;
    }

    function addProduct(string memory _name, string memory _origin) public {
        productCount++;
        products[productCount] = Product(productCount, _name, _origin, new string[](0));
        emit ProductAdded(productCount, _name, _origin);
    }

    function updateProduct(uint _id, string memory _update) public {
        require(_id > 0 && _id <= productCount, "Product does not exist.");
        products[_id].history.push(_update);
        emit ProductUpdated(_id, _update);
    }

    function getProduct(uint _id) public view returns (uint, string memory, string memory, string[] memory) {
        require(_id > 0 && _id <= productCount, "Product does not exist.");
        Product memory p = products[_id];
        return (p.id, p.name, p.origin, p.history);
    }

    function getProductCount() public view returns (uint) {
        return productCount;
    }
}