Diseño y modelación de cristales fotónicos
===========================================

.. _`github`: https://github.com/FBMA-research/photonics

Título:
-------

Diseño y modelación de cristales fotónicos

Nombres de los autores:
-----------------------

Leandro Uribe
Álvaro Bedoya

Datos de contacto:
------------------

luribe671@soyudemedellin.edu.co
ahbedoya@udemedellin.edu.co

Semillero:
----------

Diseño, caracterización y modelación de nuevos materiales

Objetivo general:
------------------

Diseñar y ajustar el cristal fotónico para aplicaciones tales como guías de onda.

Objetivos específicos:
-----------------------

- Manejar los de paquetes de uso libre (MEEP/Python) para la modelación y simulación de cristales fotónicos.
- Ajustar los ejemplos brindados por la documentación del paquete MEEP/Python a la simulación con los elementos de interés.
- Estructurar la documentación del software personalizado en `github`_.

Estado del arte.
----------------

Cristales fotónicos
~~~~~~~~~~~~~~~~~~

Los cristales fotónicos (CF) son materiales ópticos con una microestrucutra periódica a escala de la longitud de la luz. Los
cristales fotónicos ofrecen un novedosa manera de manipular las ondas electromagnéticas, ellos operan bajo el principio de
los gaps fotónicos, regiones donde los fotones no pueden propagarse [1]. Los CF se clasifican en 1D, 2D y 3D basados en la
periodicidad de la estructura [2]. Estos materiales tienen aplicaciones in guías de onda filtros ópticos y circuitos fotónicos
integrados [3].

Ecuaciones de Maxwell en la simulación de cristales fotónicos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las ecuaciones de Maxwell son el fundamento para comprender el comportamiento electromagnético de los CF [4]. La aplicación de
condiciones periódicas adecuadas es crucial para la simulación y resultados consistentes [5]. Métodos como elementos finitos
(FDTD) y plano de expansión de onda (PWE) son usados para resolver las ecuaciones de Maxwell en este contexto [6].

Desarrollo histórico.
~~~~~~~~~~~~~~~~~~~~

El concepto de CF fue introducido en los años 80 y esto represento contribuciones tanto teóricas como experimentales [7].
Investigadores como Eli Yablonovitch and Sajeev John han hecho desarrollos pioneros en este campo [8].

El software MEEP
~~~~~~~~~~~~~~~~

Meep ofrece una plataforma para la simulación de una amplia matriz de arreglos fotónicos [9]. Algunas de sus ventajas es que es
de  uso libre y es flexible para ser modificado por el usuario [10]. Algunas de sus limitaciones es el largo tiempo de computo
para simulaciones 3D [11].

Aplicaciones tecnológicas recientes de los CF.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- En comunicaciones ópticas: Usado en la creación switches ultra rápidos [12].
- Sensado: Potencial para biosensores altamente sensibles [13].
- Recolección de energía: Los CF pueden mejorar la eficiencia de las celdas solares [14].

Enfoques y limitaciones existentes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Además de Meep también existen otras herramientas como COMSOL y Lumerical, pero tienen sus limitaciones [15].  La teoría del medio
eficaz y la teoría del modo acoplado son algunos de los enfoques analíticos [16]. Los métodos actuales suelen pasar por alto los
efectos no lineales y los fenómenos cuánticos [17].

Perspectiva del futuro
~~~~~~~~~~~~~~~~~~~~~~

El aprendizaje automático y la computación cuántica son vías potenciales para mejorar las simulaciones [18]. La investigación sobre
fotónica topológica y efectos cuánticos podría revolucionar este campo [19].

Metodología
-----------

La metodología de investigación para el modelado de cristales fotónicos a partir de MEEP está basada en las siguientes fases:

Fase 1. Revisión de la literatura.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Revisión de literatura que está comprendida en el apartado anterior llamado “Estado del arte” que involucra los desarrollos
experimentales y simulados de cristales fotónicos. Igualmente los modelos físicos necesarios para las implementaciones tales como la
teórica electromagnética que se incluyen en el apartado del “Estado del arte”.

Fase 2. Definición del problema.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hipótesis: Es posible ajustar el diseño de los cristales fotónicos que permita el desarrollo posterior de guías de ondas, lentes
fotónicos y sensores.

Fase 3. Instalación del software libre MEEP y definición de parámetros.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se instaló el software MEEP cubriendo los requerimientos mínimos de funcionamiento tanto en hardware como en software. Se definieron
las condiciones del cristal fotónico tales constantes dieléctricas, constantes de red e interpolación de las zonas de Brillouin.

Fase 4. Ajuste del solver.
~~~~~~~~~~~~~~~~~~~~~~~~~~

Se incorporó software personalizado para la creación de la geometría del cristal fotónico, el ajuste de la resolución y del solver.
Se realizaron pruebas previas para la calibración a partir del comparativo brindado por el software COMSOL.

Fase 5. Captura de datos y post procesamiento de la información.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se espera en este paso el desarrollo de nuevos algoritmos en softwares como Python, Matlab o R para los cálculos adicionales que se
requieran para la presentación de los resultados.

Fase 6. Validación.
~~~~~~~~~~~~~~~~~~~

Se espera realizar comparativos con trabajos experimentales y simulados de nuestro desarrollo para validar los resultados obtenidos
de nuestras simulaciones.

Fase 7. Presentación de resultados y trabajo futuro.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se presentarán resultados parciales y definitivos dependiendo del avance del proyecto de investigación y del avance de la escritura
del artículo.

Resultados preliminares
-----------------------

Se logró replicar los resultados de las dispersiones del cristal a partir de simulaciones iniciales con el uso del software COMSOL
comparando el modo TM y añadiendo los modos TE y TM calculados en el software libre MEEP.

Se anexó un diseño personalizado en MEEP para la incorporación de las geometrías específicas del cristal fotónico.

Se está implementando la documentación del desarrollo `github`_.

Conclusiones
------------

Las implementaciones de software libre como el Meep permiten un ajuste personalizado del software a las necesidades de simulación.
Con esta plataforma tecnológica se agregaron nuevas implementaciones para la captura de las geometrías y el ajuste de la zona de
Brillouin.

Se está adaptando el software para el cómputo en un cluster que nos permita hacer simulaciones más robustas con un amplio número de
variables a estudiar.

Referencias
------------

[1] J.D. Joannopoulos, S.G. Johnson, J.N. Winn, and R.D. Meade, "Photonic Crystals: Molding the Flow of Light," Princeton University Press, 2nd ed., 2011.

[2] K. Sakoda, "Optical Properties of Photonic Crystals," Springer-Verlag, 2001.

[3] M. Qiu, "Photonic Crystals: Principles and Applications," CRC Press, 2014.

[4] A. Taflove and S.C. Hagness, "Computational Electrodynamics: The Finite-Difference Time-Domain Method," Artech House, 3rd ed., 2005.

[5] P. Yeh, "Optical Waves in Layered Media," John Wiley & Sons, 1988.

[6] K.S. Kunz and R.J. Luebbers, "The Finite Difference Time Domain Method for Electromagnetics," CRC Press, 1993.

[7] E. Yablonovitch, "Inhibited Spontaneous Emission in Solid-State Physics and Electronics," Physical Review Letters, 58, 2059 (1987).

[8] S. John, "Strong Localization of Photons in Certain Disordered Dielectric Superlattices," Physical Review Letters, 58, 2486 (1987).

[9] A. Oskooi et al., "Meep: A flexible free-software package for electromagnetic simulations by the FDTD method," Computer Physics Communications, 181(3), 687-702 (2010).

[10] C. Luo, S.G. Johnson, J.D. Joannopoulos, and J.B. Pendry, "All-angle negative refraction without negative effective index," Physical Review B, 65, 201104 (2002).

[11] D. M. Beggs, T.F. Krauss, "Compact photonic crystal circulator with flat-top transmission band created using topology optimization," Applied Physics Letters, 100, 031111 (2012).

[12] B. Maes, P. Bienstman, R. Baets, "Switching in coupled nonlinear photonic-crystal resonators," Journal of the Optical Society of America B, 22(7), 1778-1784 (2005).

[13] S.Y. Lin et al., "Enhanced Sensing Capability of Photonic Crystal Structures," Optics Letters, 29(17), 2016-2018 (2004).

[14] H.A. Atwater and A. Polman, "Plasmonics for improved photovoltaic devices," Nature Materials, 9, 205-213 (2010).

[15] M. Fallahi and A.A. Eftekhar, "COMSOL Multiphysics® Simulation of 3D Single-Mode Photonic Crystal Cavity," COMSOL Conference, Boston (2010).

[16] M. Soljačić et al., "Optimal bistable switching in nonlinear photonic crystals," Physical Review E, 66, 036611 (2002).

[17] D. R. Smith et al., "Composite Medium with Simultaneously Negative Permeability and Permittivity," Physical Review Letters, 84, 4184-4187 (2000).

[18] Z. Liu et al., "Machine Learning Photonic Structures with Complex Geometries," Nature Communications, 9, 4959 (2018).

[19] L. Lu, J.D. Joannopoulos, and M. Soljačić, "Topological Photonics," Nature Photonics, 8, 821-829 (2014).
