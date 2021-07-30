import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './inicio/inicio.component';
import { ProductoComponent } from './producto/producto.component';
import { CarritoComponent } from './carrito/carrito.component';
import { DireccionComponent } from './direccion/direccion.component';
import { MetodoPagoComponent } from './metodo-pago/metodo-pago.component';
import { MisProductosComponent } from './mis-productos/mis-productos.component';
import { CompraFinalizadaComponent } from './compra-finalizada/compra-finalizada.component';
import { CrearResenaComponent } from './crear-resena/crear-resena.component';
import { VerResenasComponent } from './ver-resenas/ver-resenas.component';

const routes: Routes = [
  {path: 'carrito', component: CarritoComponent},
  {path: 'metodo-pago', component: MetodoPagoComponent},
  {path: 'inicio', component: InicioComponent},
  {path: 'producto/:id', component: ProductoComponent},
  {path: 'direccion', component: DireccionComponent},
  {path: 'mis-productos', component: MisProductosComponent},
  {path: 'compra-finalizada', component: CompraFinalizadaComponent},
  {path: 'crear-resena', component: CrearResenaComponent},
  {path: 'ver-resenas', component: VerResenasComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
