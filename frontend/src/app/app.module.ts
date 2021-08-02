import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CarritoComponent } from './carrito/carrito.component';
import { MetodoPagoComponent } from './metodo-pago/metodo-pago.component';
import { InicioComponent } from './inicio/inicio.component';
import { ProductoComponent } from './producto/producto.component';
import { TarjetaProductoComponent } from './tarjeta-producto/tarjeta-producto.component';
import { MasVendidosComponent } from './mas-vendidos/mas-vendidos.component';
import { TodosComponent } from './todos/todos.component';
import { DireccionComponent } from './direccion/direccion.component';
import { TarjetaAdminComponent } from './tarjeta-admin/tarjeta-admin.component';
import { MisProductosComponent } from './mis-productos/mis-productos.component';
import { CompraFinalizadaComponent } from './compra-finalizada/compra-finalizada.component';
import { ResenasComponent } from './resenas/resenas.component';
import { CrearResenaComponent } from './crear-resena/crear-resena.component';
import { VerResenasComponent } from './ver-resenas/ver-resenas.component';
import { FormAltaProductoComponent } from './form-alta-producto/form-alta-producto.component';
import { CarouselModule } from 'primeng/carousel';
import { LoginComponent } from './login/login.component';
import { BarraNavCompradorComponent } from './barra-nav-comprador/barra-nav-comprador.component';
import { BarraNavVendedorComponent } from './barra-nav-vendedor/barra-nav-vendedor.component';
import { BarraNavLogComponent } from './barra-nav-log/barra-nav-log.component';

import { HttpClientModule } from '@angular/common/http';



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
    BarraNavLogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    FormsModule, // Para las entradas (inputs) o formularios
    CarouselModule, //Para mostrar los productos en Todos
    HttpClientModule //Para hacer peticiones
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
