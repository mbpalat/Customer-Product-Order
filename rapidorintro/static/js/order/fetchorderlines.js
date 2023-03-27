let fetch = new Vue({
    el   : '#vue-app-fetchorderlines',
    delimiters: ['[[', ']]'],
    data : {
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
        orderlines      :   [],
        products        :   [],
        modaltitle      :   '',
        oid             :   '',
        cid             :   '',
    },
    methods : {
        deleteorderline(oid){
            let url = '/order/deleteorderline/'+oid
            axios.get(url).then((response) => {
                let data = response.data
            })
            window.location.reload()
        },
        editorderline(cid){
            $('.save').hide();
            $('.update').show();
            $('.modal').show();
            this.modaltitle  = 'Edit Order Line'
            let url = '/order/fetchsingleorderline/'+cid
            axios.get(url).then((response) => {
                let data = response.data
                var orderline = data.orderline[0]
                this.id              =   orderline.id
                this.ordernumber     =   orderline.ordernumber
                this.orderlinenumber =   orderline.orderlinenumber
                this.productcode     =   orderline.productcode
                this.productname     =   orderline.productname
                this.customerid      =   orderline.customerid
                this.date            =   orderline.date
                this.productid       =   orderline.productid
                this.quantity        =   orderline.quantity
                this.price           =   orderline.price
            })
        },
        hidemodal(){
            $('.modal').hide();
        },
        addorderline(){
            this.id              =   '',
            this.orderlinenumber =   '',
            this.productcode     =   '',
            this.productname     =   '',
            this.productid       =   '',
            this.quantity        =   '',
            this.price           =   '',
            this.modaltitle      = 'Add Order Line'
            $('.save').show();
            $('.update').hide();
            $('.modal').show();
        },
        saveorderline(){
            if(this.ordernumber && this.orderlinenumber && this.productid && 
                this.quantity && this.price){
                    let url = '/product/fetchsingleproduct/'+this.productid
                    axios.get(url).then((response) => {
                        let data = response.data
                        var product = data.products[0]
                        this.productid         = product.id
                        this.productname       = product.name
                        this.productcode       = product.code
                        let ourl = '/order/saveorderline'
                        let body =  {
                            'ordernumber'     :   this.ordernumber,
                            'orderlinenumber' :   this.orderlinenumber,
                            'productcode'     :   this.productcode,
                            'productname'     :   this.productname,
                            'customerid'      :   this.customerid,
                            'productid'       :   this.productid,
                            'quantity'        :   this.quantity,
                            'price'           :   this.price,
                        }
                        axios.post(ourl, body).then((response) => {
                            let data = response.data
                        })
                    })
                
            }
            $('.modal').hide();
            window.location.reload()
        },
        updateorderline : function(){ 
            if(this.ordernumber && this.orderlinenumber && this.productid && 
                this.quantity && this.price){
                    let url = '/product/fetchsingleproduct/'+this.productid
                    axios.get(url).then((response) => {
                        let data = response.data
                        var product = data.products[0]
                        this.productid         = product.id
                        this.productname       = product.name
                        this.productcode       = product.code
                        let url = '/order/editorderline'
                        let body =  {
                            'id'              :   this.id,
                            'ordernumber'     :   this.ordernumber,
                            'orderlinenumber' :   this.orderlinenumber,
                            'productcode'     :   this.productcode,
                            'productname'     :   this.productname,
                            'customerid'      :   this.customerid,
                            'productid'       :   this.productid,
                            'quantity'        :   this.quantity,
                            'price'           :   this.price,
                        }
                        axios.post(url, body).then((response) => {
                            let data = response.data
                        })
                    })
            }
            $('.modal').hide();
            window.location.reload()
        },
        gotoprev(){
            window.location.href = "/order";
        },
        changeItem: function changeItem(event) {
            this.productid =  event.target.value;
        },
    },
    mounted() {
            var href = window.location.href;
            var oidslash = href.lastIndexOf('/');
            this.oid = href.substring(oidslash+1);

            let url = '/order/fetchorderlinesbyord/'+this.oid
            axios.get(url).then((response) => {
                let data = response.data
                this.orderlines = data.orderlinelist
            })

            let curl = '/product/fetchproducts'
            axios.get(curl).then((response) => {
                let data = response.data
                this.products = data.productlist
            })

            let ourl = '/order/fetchsingleorder/'+this.oid
            axios.get(ourl).then((response) => {
                let data = response.data
                var order = data.orders[0]
                this.ordernumber    = order.id
                this.customerid     = order.customerid
            })
    },
    
});

