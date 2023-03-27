let fetch = new Vue({
    el   : '#vue-app-fetchproduct',
    delimiters: ['[[', ']]'],
    data : {
        id              :   '',
        name            :   '',
        code            :   '',
        unit            :   '',
        price           :   '',
        tax             :   '',
        percent         :   '',
        products        :   [],
        index           :   0,
        modaltitle      :   '',
    },
    methods : {
        deleteproduct(cid){
            let url = '/product/deleteproduct/'+cid
            axios.get(url).then((response) => {
                let data = response.data
            })
            window.location.reload()
        },
        editproduct(cid){
            $('.save').hide();
            $('.update').show();
            $('.modal').show();
            this.modaltitle  = 'Edit Product'
            let url = '/product/fetchsingleproduct/'+cid
            axios.get(url).then((response) => {
                let data = response.data
                var product = data.products[0]
                this.id         = product.id
                this.name       = product.name
                this.code       = product.code
                this.unit       = product.unit
                this.price      = product.price
                this.tax        = product.tax
                this.percent    = product.percent
            })
        },
        hidemodal(){
            $('.modal').hide();
        },
        addproduct(){
            this.id         = ''
            this.name       = ''
            this.code       = ''
            this.unit       = ''
            this.price      = ''
            this.tax        = ''
            this.percent    = ''
            this.modaltitle     = 'Add Product'
            $('.save').show();
            $('.update').hide();
            $('.modal').show();
        },
        saveproduct(){
            if(this.name && this.code && this.unit &&
                this.price && this.tax && this.percent){
                let url = '/product/saveproduct'
                let body =  {
                    'name'       : this.name,
                    'code'       : this.code,
                    'unit'       : this.unit,
                    'price'      : this.price,
                    'tax'        : this.unit,
                    'percent'    : this.percent,
                }
                axios.post(url, body).then((response) => {
                    let data = response.data
                })
            }
            $('.modal').hide();
            window.location.reload()
        },
        updateproduct : function(){ 
            if(this.name && this.code && this.unit &&
                this.price && this.tax && this.percent){
                let url = '/product/editproduct'
                let body =  {
                    'id'         : this.id,
                    'name'       : this.name,
                    'code'       : this.code,
                    'unit'       : this.unit,
                    'price'      : this.price,
                    'tax'        : this.unit,
                    'percent'    : this.percent,
                }
                axios.post(url, body).then((response) => {
                    let data = response.data
                })
            }
            $('.modal').hide();
            window.location.reload()
        },
    },
    mounted() {
            let url = '/product/fetchproducts'
            axios.get(url).then((response) => {
                let data = response.data
                this.products = data.productlist
            })
    },
    
});

