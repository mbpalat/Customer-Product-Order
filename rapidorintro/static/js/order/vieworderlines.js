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
        modaltitle      :   '',
        oid             :   '',
    },
    methods : {
        gotoprev(){
            window.location.href = "/order";
        }
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
    },
    
});

