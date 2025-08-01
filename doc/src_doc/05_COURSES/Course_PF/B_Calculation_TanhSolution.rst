.. _Calculation-Tanh-Solution:

Appendix B: solutions of one-dimensional Euler-Lagrange 
=======================================================

In this appendix we detail the main stages to obtain the solution of:

.. math::
   :label: Euler_Lagrange_1D

   \zeta\frac{d^{2}\phi}{dx^{2}}-H\frac{dg(\phi)}{d\phi}=0

We demonstrate that the solution has a hyperbolic tangent profile for several choices of double-wells g(\phi).

Equivalent form of 1D Euler-Lagrange
------------------------------------

First, we multiply Eq. :eq:`Euler_Lagrange_1D` by :math:`d\phi/dx`:

.. math::
   :label:

   \zeta\frac{d\phi}{dx}\frac{d^{2}\phi}{dx^{2}}-H\frac{d\phi}{dx}\frac{dg(\phi)}{d\phi}=0
      
The first term is the derivative of :math:`d\phi/dx` squared, whereas the second one becomes a derivative wrt :math:`x`:

.. math::
   :label:

   \frac{\zeta}{2}\frac{d}{dx}\left(\frac{d\phi}{dx}\right)^{2}-H\frac{dg(\phi)}{dx}=0

We obtain a first result that will be used for the calculation of the surface tension in :ref:`Calculation-Surface-Tension`:

.. math::
   :label: Equality_For_Surface_Tension

   \boxed{\frac{\zeta}{2}\left(\frac{d\phi}{dx}\right)^{2}=Hg(\phi)}

The second result derives from that relation by keeping the positive root :math:`d\phi/dx=\sqrt{2Hg(\phi)/\zeta}`. We obtain one relation between :math:`dx` and :math:`d\phi`:

.. math::
   :label: eq:Chgt_Variable

   dx=\frac{1}{\sqrt{2Hg(\phi)/\zeta}}d\phi

That relation will be useful for variable change by transforming the integral on :math:`x` into integral on :math:`\phi`. That relation is equivalent to:

.. math::
   :label: eq:Egalite_DP-2

   \boxed{\frac{d\phi}{dx}=\sqrt{2\frac{H}{\zeta}g(\phi)}}

Case :math:`g_1(\phi)=\phi^2(1-\phi)^2`
---------------------------------------

If we choose :math:`g(\phi)=g_1(\phi)=\phi^2(1-\phi)^2`, then we obtain:

.. math::
   :label:

   \frac{d\phi}{dx}=\sqrt{2\frac{H}{\zeta}}\phi(1-\phi)

L'équation s'écrit simplement :math:`d\phi/\phi(1-\phi)=Cdx` with :math:`C=\sqrt{2H/\zeta}`, that, once integrated is equal to: :math:`\ln(\phi)-\ln(1-\phi)=Cx`. By applying the exponential on both sides and making appear the factor 2 inside the right-hand side, we obtain: :math:`\phi/(1-\phi)=\exp\left[2(Cx/2)\right]`. Next we compute separately  :math:`\exp\left[2(Cx/2)\right]-1` and :math:`\exp\left[2(Cx/2)\right]+1`. We express those two expressions with :math:`\phi` and we take the ratio (let us remind that :math:`\tanh(X)=(e^{2X}-1)/(e^{2X}+1)`). We find: :math:`2\phi-1=\tanh(Cx/2)`. Finally by replacing  :math:`C` by :math:`C=\sqrt{2H/\zeta}`, we obtain:

.. math::
   :label:

   \phi(x)=\frac{1}{2}\left[1+\tanh\left(\frac{1}{2}\sqrt{\frac{2H}{\zeta}}x\right)\right]
   
We make appear inside the hyperbolic tangent function the simplified form :math:`2x/W`, we obtain:

.. math::
   :label:

   \boxed{\phi(x)=\frac{1}{2}\left[1+\tanh\left(\frac{2x}{W}\right)\right]}
   
where the interface width is defined by:

.. math::
   :label:

   \boxed{W=\sqrt{\frac{8\zeta}{H}}}

Case :math:`g_{2}(\phi)=(\phi_{l}-\phi)^{2}(\phi-\phi_{g})^{2}`
------------------------------------------------------------------------------

We start from Eq. :eq:`eq:Egalite_DP-2` by using :math:`g_{2}(\phi)=(\phi_{l}-\phi)^{2}(\phi-\phi_{g})^{2}` where :math:`\phi_{g}<\phi<\phi_{l}`. After integration of :math:`d\phi/(\phi_{l}-\phi)(\phi-\phi_{g})=Cdx`, we obtain :math:`\ln(\phi-\phi_{g})-\ln(\phi_{l}-\phi)=(\phi_{l}-\phi_{g})Cx`. We make appear the ratio :math:`(\phi-\phi_{g})/(\phi_{l}-\phi)` inside a unique logarithmic function, next we apply the exponential function to both members of equality with a factor 2 in the right-hand side: :math:`(\phi-\phi_{g})/(\phi_{l}-\phi)=\exp\left[2(\phi_{l}-\phi_{g})Cx/2\right]`.

We set :math:`X=(\phi_{l}-\phi_{g})Cx/2`, to make appear the hyperbolic tangent function (like in previous section), we calculate separately :math:`e^{2X}-1` and :math:`e^{2X}+1` and we make the ratio. We obtain:

.. math::
   :label:

   \frac{e^{2X}-1}{e^{2X}+1}=\tanh\left[\frac{(\phi_{l}-\phi_{g})}{2}Cx\right]=\frac{2\phi-(\phi_{l}+\phi_{g})}{\phi_{l}-\phi_{g}}
   
Finally we obtain:

.. math::
   :label: 

   \phi(x)=\frac{\phi_{l}+\phi_{g}}{2}+\frac{\phi_{l}-\phi_{g}}{2}\tanh\left[\frac{(\phi_{l}-\phi_{g})}{2}\sqrt{\frac{2H}{\zeta}}x\right]
   
We make appear inside the hyperbolic tangent function the simplified expression 2x/W:

.. math::
   :label: eq:Sol_TanH_rhol_rhog

   \boxed{\phi(x)=\frac{\phi_{l}+\phi_{g}}{2}+\frac{\phi_{l}-\phi_{g}}{2}\tanh\left[\frac{2x}{W}\right]}
   
with the interface width defined by:

.. math::
   :label:

   \boxed{W=\frac{4}{(\phi_{l}-\phi_{g})}\sqrt{\frac{\zeta}{2H}}}

Case :math:`g_{3}(\phi)=(\phi^{\star}-\phi)^{2}(\phi^{\star}+\phi)^{2}`
--------------------------------------------------------------------------------------

This is a particular case of :math:`g_{2}(\phi)` with :math:`\phi_{l}=\phi^{\star}` and :math:`\phi_{g}=-\phi^{\star}`. With those variable changes Eq. :eq:`eq:Sol_TanH_rhol_rhog` becomes
 
.. math::
   :label:

   \boxed{\phi(x)=\phi^{\star}\tanh\left[\frac{2x}{W}\right]}
   
with an interface width defined by
 
.. math::
   :label:

   \boxed{W=\frac{1}{\phi^{\star}}\sqrt{\frac{2\zeta}{H}}}

**Proof**

We check by starting from Eq. :eq:`eq:Egalite_DP-2` en utilisant :math:`g_{3}(\phi)=(\phi^{\star}-\phi)^{2}(\phi^{\star}+\phi)^{2}` where :math:`-\phi^{\star}<\phi<\phi^{\star}`. By integrating :math:`d\phi/(\phi^{\star}-\phi)(\phi^{\star}+\phi)=Cdx`, we obtain :math:`\ln(\phi^{\star}+\phi)-\ln(\phi^{\star}-\phi)=2\phi^{\star}Cx`. After application of exponential function: :math:`\exp\left[2\phi^{\star}Cx\right]=(\phi^{\star}+\phi)/(\phi^{\star}-\phi)`. Relation à partir de laquelle on en déduit simplement :math:`\phi`:

.. math::

   \phi(x)=\phi^{\star}\tanh\left(\phi^{\star}\sqrt{\frac{2H}{\zeta}}x\right)

With simple form :math:`2x/W` inside the hyperbolic tangent:

.. math::

   \phi(x)=\phi^{\star}\tanh\left(\frac{2x}{W}\right)

with

.. math::

   W=\frac{1}{\phi^{\star}}\sqrt{\frac{2\zeta}{H}}