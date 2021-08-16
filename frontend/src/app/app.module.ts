import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CarritoComponent } from './modules/carrito/carrito.component';
import { MetodoPagoComponent } from './modules/metodo-pago/metodo-pago.component';
import { InicioComponent } from './modules/inicio/inicio.component';
import { ProductoComponent } from './modules/producto/producto.component';
import { TarjetaProductoComponent } from './modules/tarjeta-producto/tarjeta-producto.component';
import { MasVendidosComponent } from './modules/mas-vendidos/mas-vendidos.component';
import { TodosComponent } from './modules/todos/todos.component';
import { DireccionComponent } from './modules/direccion/direccion.component';
import { TarjetaAdminComponent } from './modules/tarjeta-admin/tarjeta-admin.component';
import { MisProductosComponent } from './modules/mis-productos/mis-productos.component';
import { CompraFinalizadaComponent } from './modules/compra-finalizada/compra-finalizada.component';
import { ResenasComponent } from './modules//resenas/resenas.component';
import { CrearResenaComponent } from './modules/crear-resena/crear-resena.component';
import { VerResenasComponent } from './modules/ver-resenas/ver-resenas.component';
import { FormAltaProductoComponent } from './modules/form-alta-producto/form-alta-producto.component';
import { CarouselModule } from 'primeng/carousel';
import { LoginComponent } from './modules/login/login.component';
import { BarraNavCompradorComponent } from './modules/barra-nav-comprador/barra-nav-comprador.component';
import { BarraNavVendedorComponent } from './modules/barra-nav-vendedor/barra-nav-vendedor.component';
import { BarraNavLogComponent } from './modules/barra-nav-log/barra-nav-log.component';

import { HttpClientModule } from '@angular/common/http';
import { SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';
import { RegistrarComponent } from './modules/registrar/registrar.component';
import { CarruselComponent } from './modules/carrusel/carrusel.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { BackgroundComponent } from './modules/background/background.component';



@NgModule({
  declarations: [
    AppComponent,
    CarritoComponent,
    MetodoPagoComponent,
    InicioComponent,
    ProductoComponent,
    TarjetaProductoComponent,
    MasVendidosComponent,
    TodosComponent,
    DireccionComponent,
    TarjetaAdminComponent,
    MisProductosComponent,
    CompraFinalizadaComponent,
    ResenasComponent,
    CrearResenaComponent,
    VerResenasComponent,
    FormAltaProductoComponent,
    LoginComponent,
    BarraNavCompradorComponent,
    BarraNavVendedorComponent,
    BarraNavLogComponent,
    RegistrarComponent,
    CarruselComponent,
    BackgroundComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    FormsModule, // Para las entradas (inputs) o formularios
    CarouselModule, //Para mostrar los productos en Todos
    HttpClientModule, //Para hacer peticiones
    ReactiveFormsModule,
    //=> Basic usage (forRoot can also take options, see the wiki)
    SweetAlert2Module.forRoot(),
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
