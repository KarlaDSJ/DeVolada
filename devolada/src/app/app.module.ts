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
<<<<<<< HEAD
import { CompraFinalizadaComponent } from './compra-finalizada/compra-finalizada.component';
=======
import { ResenasComponent } from './resenas/resenas.component';
import { CrearResenaComponent } from './crear-resena/crear-resena.component';
>>>>>>> 86f12f7312af2fa3c1885fd7f828c7b32532aae2


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
<<<<<<< HEAD
    CompraFinalizadaComponent
=======
    ResenasComponent,
    CrearResenaComponent
>>>>>>> 86f12f7312af2fa3c1885fd7f828c7b32532aae2
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    FormsModule // Para las entradas (inputs) o formularios
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
