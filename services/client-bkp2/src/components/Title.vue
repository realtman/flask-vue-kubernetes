<template>
<!-- Header -->
<div class="header mt-md-5">
    <div class="header-body">
        <div class="row align-items-center">
            <div class="col">

                <!-- Pretitle -->
                <h6 class="header-pretitle">
                    {{subtitle | capitalize}}
                </h6>

                <!-- Title -->
                <h1 class="header-title">
                    {{title}}
                </h1>

            </div>
        </div> <!-- / .row -->
    </div>
</div>
</template>

<script>
export default {
    name: 'inari-title',
    props: {
        subtitle: String,
        title: String,

    },
    data: function () {
        return {
        }
    },
    filters: {
        capitalize: function (str) {
            return str.charAt(0).toUpperCase() + str.slice(1)
        }
    }

}
</script>
