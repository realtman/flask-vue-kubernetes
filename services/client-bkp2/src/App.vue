<template>
<div id="app">

    <!-- Modal: Demo -->
    <div class="modal fade fixed-right" id="modalDemo" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-vertical" role="document">
            <form class="modal-content" id="demoForm">

                <div class="modal-body">

                    <!-- Close -->
                    <a class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </a>

                    <div class="text-center">
                        <img src="./assets/img/illustrations/designer-life.svg" alt="..." class="img-fluid mb-3">
              </div>

                        <h2 class="text-center mb-2">
                            Make Dashkit Your Own
                        </h2>

                        <p class="text-center mb-4">
                            Set preferences that will be cookied for your live preview demonstration.
                        </p>

                        <hr class="mb-4">

                        <h4 class="mb-1">
                            Color Scheme
                        </h4>

                        <p class="small text-muted mb-3">
                            Overall light or dark presentation.
                        </p>

                        <div class="btn-group-toggle d-flex mb-4" data-toggle="buttons">
                            <label class="btn btn-white active col">
                  <input type="radio" name="colorScheme" id="colorSchemeLight" value="light" checked> <i class="fe fe-sun mr-2"></i> Light Mode
                </label>
                            <label class="btn btn-white col ml-2">
                  <input type="radio" name="colorScheme" id="colorSchemeDark" value="dark"> <i class="fe fe-moon mr-2"></i> Dark Mode
                </label>
                        </div>

                        <h4 class="mb-1">
                            Navigation Position
                        </h4>

                        <p class="small text-muted mb-3">
                            Select the primary navigation paradigm for your app.
                        </p>

                        <div class="btn-group-toggle d-flex mb-4" data-toggle="buttons">
                            <label class="btn btn-white active col">
                  <input type="radio" name="navPosition" id="navPositionSidenav" value="sidenav" checked> Sidenav
                </label>
                        </div>

                        <h4 class="mb-1">
                            Sidebar Color
                        </h4>

                        <p class="small text-muted mb-3">
                            Usually dictated by the color scheme, but can be overriden.
                        </p>

                        <div class="btn-group-toggle d-flex mb-4" data-toggle="buttons">
                            <label class="btn btn-white active col">
                  <input type="radio" name="sidebarColor" id="sidebarColorDefault" value="default" checked> Default
                </label>
                            <label class="btn btn-white col ml-2">
                  <input type="radio" name="sidebarColor" id="sidebarColorVibrant" value="vibrant"> Vibrant
                </label>
                        </div>

                    </div>
                    <div class="modal-footer border-0">

                        <button type="submit" class="btn btn-block btn-primary mt-auto">
              Preview
            </button>

                    </div>
            </form>
        </div>
    </div>

    <!-- NAVIGATION
    ================================================== -->

    <nav class="navbar navbar-vertical fixed-left navbar-expand-md navbar-light" id="sidebar">
        <div class="container-fluid">

            <!-- Toggler -->
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#sidebarCollapse" aria-controls="sidebarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

            <!-- Brand -->
            <a class="navbar-brand" href="/">
            <img src="./assets/img/logo.svg" class="navbar-brand-img 
            mx-auto" alt="...">
          </a>

            <!-- Collapse -->
            <div class="collapse navbar-collapse" id="sidebarCollapse">

                <!-- Navigation -->
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="#sidebarDashboards" data-toggle="collapse" role="button" aria-expanded="true" aria-controls="sidebarDashboards">
                  <i class="fe fe-terminal"></i> Seed Supply
                </a>
                        <div class="collapse show" id="sidebarDashboards">
                            <ul class="nav nav-sm flex-column">
                                <li class="nav-item">
                                    <router-link to="{ name: 'CCDView'}" class="nav-link ">
                                        CCD
                                    </router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link to="{ name: 'JobListView'}" class="nav-link ">
                                        Job lists
                                    </router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link to="{ name: 'JobCreateComponent'}" class="nav-link">
                                        Create Job
                                    </router-link>
                                </li>
                                <!-- LHB TODO: REMOVE ME -->
                                <li class="nav-item">
                                    <router-link to="{ name: 'RestApiExampleView'}" class="nav-link ">
                                        Demo RestApiView
                                    </router-link>
                                </li>
                            </ul>
                        </div>
                    </li>
                </ul>

                <!-- Divider -->
                <hr class="navbar-divider my-3">

                <!-- Push content down -->
                <div class="mt-auto"></div>

                <!-- Customize -->
                <a href="#modalDemo" class="btn btn-block btn-primary mb-4" data-toggle="modal">
              <i class="fe fe-sliders mr-2"></i> Customize
            </a>

            </div> <!-- / .navbar-collapse -->

        </div>
    </nav>
    <!-- MAIN CONTENT
    ================================================== -->
    <div class="main-content">
        <div class="container-fluid">
            <div class="row justify-content-center">
                <div class="col-12">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div> <!-- / .main-content -->
</div>
</template>

<script>
export default {
    name: 'app',
}
</script>