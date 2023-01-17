class service_details{
    constructor(srvc_name,srvc_description,srvc_price){
        this.srvc_name = srvc_name
        this.srvc_description = srvc_description
        this.srvc_price = srvc_price
    }

    render_html(){
        return `<div class="card-service">
        <div class="row">
          <div class="col-md-12 col-lg-3 col-xl-3 mb-4 mb-lg-0">
            <div class="bg-image hover-zoom ripple rounded ripple-surface">
              <img src="https://img.icons8.com/windows/96/20C997/dental-braces.png" class="w-100" />
              <a href="#!">
                <div class="hover-overlay">
                  <div class="mask" style="background-color: rgba(253, 253, 253, 0.15);"></div>
                </div>
              </a>
            </div>
          </div>
          <div class="col-md-6 col-lg-6 col-xl-6 sub-2">
            <h5 class="service-name">${this.srvc_name}</h5>
            <p class="text-truncate mb-4 mb-md-0">
              There are many variations of passages of Lorem Ipsum available
            </p>
          </div>
          <div class="col-md-6 col-lg-3 col-xl-3 border-sm-start-none border-start">
            <div class="d-flex flex-row align-items-center mb-1">
              <h6 class="mb-1 me-1" style="overflow: hidden;">P${this.srvc_price}</h6>
            </div>
            <div class="d-flex flex-column mt-4">
              <button class="btn btn-primary btn-sm" onclick="redirect_booking()" type="button">Book</button>
            </div>
          </div>
        </div>
      </div>`
    }
}