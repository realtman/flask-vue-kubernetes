<template id="job-status">
  <div class="main-content">

    <div class="container-fluid">
      <div class="row justify-content-center">
        <div class="col-12">

          <!-- Header -->
          <div class="header mt-md-5">
            <div class="header-body">
              <div class="row align-items-center">
                <div class="col">

                  <!-- Pretitle -->
                  <h6 class="header-pretitle">
                    Status
                  </h6>

                  <!-- Title -->
                  <h1 class="header-title">
                    {{ gene }}
                  </h1>

                </div>
              </div> <!-- / .row -->
            </div>
          </div>

          <!-- Card -->
          <div class="card" data-toggle="lists">
            <ul class="list-group">
              <li class="list-group-item">{{ statusList.jobId.name }}: {{ statusList.jobId.value }} </li>
              <li class="list-group-item">{{ statusList.status.name }}:
                <div v-if="statusList.status.value === 'in progress'">
                  <div class="badge badge-soft-warning">In Progress</div>
                  <div class="spinner-border text-primary" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>
                </div>
              </li>
              <li class="list-group-item">{{ statusList.benchlingUrl.name }}: <a :href=statusList.benchlingUrl.link>{{ statusList.benchlingUrl.value }}</a></li>
              <li class="list-group-item">{{ statusList.s3Url.name }}: <a :href=statusList.s3Url.link>{{ statusList.s3Url.value }}</a></li>
            </ul>
          </div>
        </div>
      </div> <!-- / .row -->
    </div>

  </div> <!-- / .main-content -->
</template>

<script>
  export default {
    name: 'job-status',
    data: function () {
        return {
            gene: "GeneID: 1459",
            statusList: {
              jobId: {
                name: "Job ID", 
                value: "i-respect-lewis"
              },
              status: {
                name: "Status", 
                value: "in progress"
              },
              benchlingUrl: {
                name: "Benchling URL", 
                link: "https://www.spacejam.com/archive/spacejam/movie/jam.htm",
                value: "spacejam.com"
              },
              s3Url: {
                name: "s3 URL",
                link: "https://www.youtube.com/watch?v=iGsSzVthbN0", 
                value: "Stan Podlk (who is that???)"
              }
            }
        }
    },
  };
</script>

