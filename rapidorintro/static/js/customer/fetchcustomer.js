let fetch = new Vue({
    el   : '#vue-app-fetchcustomer',
    delimiters: ['[[', ']]'],
    data : {
        id              : '',
        customername    : '',
        username        : '',
        mobile          : '',
        customers       : [],
        index           : 0,
        modaltitle      : '',
    },
    methods : {
        deletecustomer(cid){
            let url = '/customer/deletecustomer/'+cid
            axios.get(url).then((response) => {
                let data = response.data
                $('#msg').val(data.message)
            })
            window.location.reload()
        },
        editcustomer(cid){
            $('.save').hide();
            $('.update').show();
            $('.modal').show();
            this.modaltitle     = 'Edit Customer'
            let url = '/customer/fetchsinglecustomer/'+cid
            axios.get(url).then((response) => {
                let data = response.data
                var customer = data.customers[0]
                this.id             = customer.id
                this.customername   = customer.customername
                this.username       = customer.username
                this.mobile         = customer.mobile
            })
        },
        hidemodal(){
            $('.modal').hide();
        },
        addcustomer(){
            this.id             = ''
            this.customername   = ''
            this.username       = ''
            this.mobile         = ''
            this.modaltitle     = 'Add Customer'
            $('.save').show();
            $('.update').hide();
            $('.modal').show();
        },
        savecustomer(){
            if(this.customername && this.username && this.mobile){
                let url = '/customer/savecustomer'
                let body =  {
                    'name'          : this.name,
                    'customername'  : this.customername,
                    'username'      : this.username,
                    'mobile'        : this.mobile,
                }
                axios.post(url, body).then((response) => {
                    let data = response.data
                })
            }
            $('.modal').hide();
            window.location.reload()
        },
        updatecustomer : function(){ 
            if(this.customername && this.username && this.mobile){
                let url = '/customer/editcustomer'
                let body =  {
                    'id'             : this.id,
                    'customername'   : this.customername,
                    'username'       : this.username,     
                    'mobile'         : this.mobile,
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
            let url = '/customer/fetchcustomers'
            axios.get(url).then((response) => {
                let data = response.data
                this.customers = data.customerlist
            })
    },
    
});

