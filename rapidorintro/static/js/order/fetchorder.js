let fetch = new Vue({
    el   : '#vue-app-fetchorder',
    delimiters: ['[[', ']]'],
    data : {
        id              : '',
        ordernumber     : '', 
        customer        : '',
        customerid      : '',
        orders          : [],
        customers       : [],
        products        : [],
        orderlines      : [],
        index           : 0,
        modaltitle      : '',
        selected        : null,
        viewurl         : '',
        orderline       :{
            id              :   '',
            ordernumber     :   '',
            orderlinenumber :   '',
            productcode     :   '',
            productname     :   '',
            customerid      :   '',
            date            :   '',
            productid       :   '',
            quantity        :   '',
            price           :   '',
        }
    },
    methods : {
        deleteorder(oid){
            let url = '/order/deleteorder/'+oid
            axios.get(url).then((response) => {
                let data = response.data
            })
            window.location.reload()
        },
        editorder(oid){
            $('.save').hide();
            $('.update').show();
            $('.modal').show();
            this.modaltitle     = 'Edit Order'
            let url = '/order/fetchsingleorder/'+oid
            axios.get(url).then((response) => {
                let data = response.data
                var order = data.orders[0]
                this.id             = order.id
                this.ordernumber    = order.ordernumber
                this.customer       = order.customer
                this.customerid     = order.customerid
            })
            this.orderline.customerid = this.customerid
        },
        hidemodal(){
            $('.modal').hide();
            window.location.reload();
        },
        fetchorder(){
            let url = '/order/fetchsingleorder/'+this.id
            axios.get(url).then((response) => {
                let data = response.data
                var order = data.orders[0]
                this.id             = order.id
                this.ordernumber    = order.ordernumber
                this.customer       = order.customer
                this.customerid     = order.customerid
            })
            $('.order').show();
            $('.orderline').hide();
            $('.fetch').hide();
            $('.update').show();
            
        },
        addorder(){
            this.id             = ''
            this.ordernumber    = ''
            this.customer       = ''
            this.customerid     = ''
            this.modaltitle     = 'Add Order'
            $('.save').show();
            $('.update').hide();
            $('.modal').show();
        },
        saveorder(){
            if(this.ordernumber && this.customerid){
                let curl = '/customer/fetchsinglecustomer/'+this.customerid
                axios.get(curl).then((response) => {
                    let data = response.data
                    var customer    = data.customers[0]
                    this.customer   = customer.customername
                    let url = '/order/saveorder'
                    let body =  {
                        'ordernumber'    : this.ordernumber,
                        'customer'       : this.customer,
                        'customerid'     : this.customerid,
                    }
                    axios.post(url, body).then((response) => {
                        let data = response.data;
                        this.id = data.id;
                    })
                })
            }
            this.orderline.customerid = this.customerid
            this.orderline.ordernumber = this.ordernumber
            $('.order').hide();
            $('.orderline').show();
            $('.save').hide();
            $('.fetch').show();
            this.modaltitle     = 'Add Order Line'
        },
        updateorder : function(){ 
            if(this.ordernumber && this.customerid){
                let curl = '/customer/fetchsinglecustomer/'+this.customerid
                axios.get(curl).then((response) => {
                    let data = response.data
                    var customer    = data.customers[0]
                    this.customer   = customer.customername
                    let url = '/order/editorder'
                    let body =  {
                    'id'             : this.id,
                    'ordernumber'    : this.ordernumber,
                    'customer'       : this.customer,
                    'customerid'     : this.customerid,
                }
                axios.post(url, body).then((response) => {
                    let data = response.data
                    let url = '/order/fetchorderlinesbyord/'+this.ordernumber
                    axios.get(url).then((response) => {
                        let data = response.data
                        this.orderlines = data.orderlinelist
                    })
                })
                })
            }
            this.orderline.ordernumber = this.ordernumber;
            $('.order').hide();
            $('.orderline').show();
            $('.update').hide();
            $('.fetch').show();
            this.modaltitle     = 'Edit Order Line'
        },
        changeItem(event) {
            this.customerid =  event.target.value;
            console.log(this.customerid);
        },
        changeProduct(event) {
            this.orderline.productid =  event.target.value;
        },
        vieworderline(oid){
            this.viewurl = "vieworderlines/"+oid
            window.location.href = this.viewurl 
        },
        editorderline(oid){
            this.viewurl = "orderlines/"+oid
            window.location.href = this.viewurl
        },
        saveorderline(){
            this.orderline.customerid = this.customerid
            if(this.orderline.ordernumber && this.orderline.orderlinenumber && this.orderline.productid && 
                this.orderline.quantity && this.orderline.price){
                    let url = '/product/fetchsingleproduct/'+this.orderline.productid
                    axios.get(url).then((response) => {
                        let data = response.data
                        var product = data.products[0]
                        this.orderline.productid         = product.id
                        this.orderline.productname       = product.name
                        this.orderline.productcode       = product.code
                        let ourl = '/order/saveorderline'
                        let body =  {
                            'ordernumber'     :   this.orderline.ordernumber,
                            'orderlinenumber' :   this.orderline.orderlinenumber,
                            'productcode'     :   this.orderline.productcode,
                            'productname'     :   this.orderline.productname,
                            'customerid'      :   this.orderline.customerid,
                            'productid'       :   this.orderline.productid,
                            'quantity'        :   this.orderline.quantity,
                            'price'           :   this.orderline.price,
                        }
                        axios.post(ourl, body).then((response) => {
                            let data = response.data
                            let url = '/order/fetchorderlinesbyord/'+this.ordernumber
                            axios.get(url).then((response) => {
                                let data = response.data
                                this.orderlines = data.orderlinelist
                            })
                        })
                    })
                
            }
        },
        deleteorderline(oid){
            let url = '/order/deleteorderline/'+oid
            axios.get(url).then((response) => {
                let data = response.data
                let url = '/order/fetchorderlinesbyord/'+this.ordernumber
                axios.get(url).then((response) => {
                    let data = response.data
                    this.orderlines = data.orderlinelist
                })
            })
        },
        
       
    },
    mounted() {
            let url = '/order/fetchorders'
            axios.get(url).then((response) => {
                let data = response.data
                this.orders = data.orderlist
            })

            let curl = '/customer/fetchcustomers'
            axios.get(curl).then((response) => {
                let data = response.data
                this.customers = data.customerlist
            })

            let purl = '/product/fetchproducts'
            axios.get(purl).then((response) => {
                let data = response.data
                this.products = data.productlist
            })

            $('.orderline').hide();
            $('.fetch').hide();
    },
    
});

