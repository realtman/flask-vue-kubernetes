<template>
  <div class="main-content">
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-12 col-lg-10 col-xl-8">

          <!-- Header -->
          <div class="header mt-md-5">
            <div class="header-body">
              <div class="row align-items-center">
                <div class="col">

                  <!-- Pretitle -->
                  <h6 class="header-pretitle">
                    New Guide
                  </h6>

                  <!-- Title -->
                  <h1 class="header-title">
                    Create a new Guide
                  </h1>

                </div>
              </div> <!-- / .row -->
            </div>
          </div>

          <!-- Form -->
          <form class="mb-4">

            <!-- Team name
            <div class="form-group">
              <label>
                Team name
              </label>
              <input type="text" class="form-control">
            </div>-->

            <div class="form-group">
              <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
                  data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Crop
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                  <a class="dropdown-item" href="#">Corn</a>
                  <a class="dropdown-item" href="#">Soy</a>
                  <a class="dropdown-item" href="#">Hannah Montana</a>
                </div>
              </div>
            </div>

            <div class="form-group">
              <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
                  data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Cultivar
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                  <a class="dropdown-item" href="#">I</a>
                  <a class="dropdown-item" href="#">Have</a>
                  <a class="dropdown-item" href="#">No</a>
                  <a class="dropdown-item" href="#">Clue</a>
                  <a class="dropdown-item" href="#">What</a>
                  <a class="dropdown-item" href="#">Goes</a>
                  <a class="dropdown-item" href="#">Here</a>
                </div>
              </div>
            </div>

            <!-- Divider -->
            <hr class="mt-4 mb-5">

            <div class="row">
              <div class="col-12 col-md-6">
                <div class="form-group">
                  <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
                      data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      Version
                    </button>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                      <a class="dropdown-item" href="#">I</a>
                      <a class="dropdown-item" href="#">Have</a>
                      <a class="dropdown-item" href="#">No</a>
                      <a class="dropdown-item" href="#">Clue</a>
                      <a class="dropdown-item" href="#">What</a>
                      <a class="dropdown-item" href="#">Goes</a>
                      <a class="dropdown-item" href="#">Here</a>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-12 col-md-6">

                <!-- Warning -->
                <div class="card bg-light border">
                  <div class="card-body">

                    <h4 class="mb-2">
                      <i class="fe fe-alert-triangle"></i> Warning
                    </h4>

                    <p class="small text-muted mb-0">
                      Some warning that describes something you shouldn't do. Like don't stick a frozen pizza in a
                      toaster.
                    </p>

                  </div>
                </div>
              </div>
            </div>

            <!-- Divider -->
            <hr class="mt-4 mb-5">

            <!-- Team members -->
            <div class="form-group">
              <label>
                Gene ID
              </label>
              <select class="form-control" data-toggle="select" multiple>
                <option>
                  Gene Belcher
                </option>
                <option>
                  Gene Wilder
                </option>
                <option>
                  Gene Simmons
                </option>
                <option>
                  Gene Snitsky
                </option>
              </select>
            </div>

            <!-- Divider -->
            <hr class="mt-4 mb-5">


            <div class="form-group">
              <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
                  data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Edit Strategy
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                  <a class="dropdown-item" href="#">I</a>
                  <a class="dropdown-item" href="#">Have</a>
                  <a class="dropdown-item" href="#">No</a>
                  <a class="dropdown-item" href="#">Clue</a>
                  <a class="dropdown-item" href="#">What</a>
                  <a class="dropdown-item" href="#">Goes</a>
                  <a class="dropdown-item" href="#">Here</a>
                </div>
              </div>
            </div>

            <!-- Divider -->
            <hr class="mt-5 mb-5">

            <!-- Buttons -->
            <a href="job-status" class="btn btn-block btn-primary">
              Create Job
            </a>
            <a href="#" class="btn btn-block btn-link text-muted">
              Cancel this Job
            </a>

          </form>

        </div>
      </div> <!-- / .row -->
    </div>
  </div> <!-- / .main-content -->
</template>
