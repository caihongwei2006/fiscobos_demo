pragma solidity ^0.8.0;

contract SupplyChain {
    struct Supplier {
        uint id;
        string name;
        string location;
    }

    struct Product {
        uint id;
        string name;
        uint quantity;
        address currentOwner;
        uint supplierId;
    }

    mapping(uint => Supplier) public suppliers;
    mapping(uint => Product) public products;
    mapping(address => uint[]) public ownerProducts;

    uint public supplierCount;
    uint public productCount;

    event SupplierAdded(uint id, string name, string location);
    event ProductAdded(uint id, string name, uint quantity, uint supplierId);
    event ProductTransferred(uint productId, address from, address to);

    function addSupplier(string memory _name, string memory _location) public {
        supplierCount++;
        suppliers[supplierCount] = Supplier(supplierCount, _name, _location);
        emit SupplierAdded(supplierCount, _name, _location);
    }

    function addProduct(string memory _name, uint _quantity, uint _supplierId) public {
        require(_supplierId > 0 && _supplierId <= supplierCount, "Invalid supplier ID");
        productCount++;
        products[productCount] = Product(productCount, _name, _quantity, msg.sender, _supplierId);
        ownerProducts[msg.sender].push(productCount);
        emit ProductAdded(productCount, _name, _quantity, _supplierId);
    }

    function transferProduct(uint _productId, address _to) public {
        require(products[_productId].currentOwner == msg.sender, "You are not the owner of this product");
        products[_productId].currentOwner = _to;
        ownerProducts[_to].push(_productId);
        emit ProductTransferred(_productId, msg.sender, _to);
    }

    function getProduct(uint _productId) public view returns (string memory, uint, address, uint) {
        Product memory product = products[_productId];
        return (product.name, product.quantity, product.currentOwner, product.supplierId);
    }
}