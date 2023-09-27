from ._anvil_designer import _TreantJsExampleTemplate
from anvil import *
import anvil.server

class _TreantJsExample(_TreantJsExampleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.node = {
        'text': { 'name': "LIFE" },
        'HTMLclass': "the-parent",
        'children': [
            {
                'text': { 'name': "true bacteria" },
                'image': "img/truebacteria.png"
            },
            {
                'pseudo': True,
                'children': [
                    {
                        'text': { 'name': "archea bacteria" },
                        'image': "img/archaebacteria.png"
                    },
                    {
                        'text': { 'name': "EUKARYOTES" },
                        'HTMLclass': "the-parent",
                        'children': [
                            {
                                'text': { 'name': "protocists" },
                                'image': "img/protoctis.png"
                            },
                            {
                                'pseudo': True,
                                'children': [
                                    {
                                        'text': { 'name': "PLANTS" },
                                        'HTMLclass': "the-parent",
                                        'children': [
                                            {
                                                'pseudo': True,
                                                'children': [
                                                    {
                                                        'pseudo': True,
                                                        'children': [
                                                            {
                                                                'pseudo': True,
                                                                'children': [
                                                                    {
                                                                        'text': { 'name': "flowering seed plants" },
                                                                        'image': "img/cvijece2.png"
                                                                    },
                                                                    {
                                                                        'text': { 'name': "non-flowering seed plants" },
                                                                        'image': "img/ne_cvijece.png"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                               'text': { 'name': "ferns and fern allies" },
                                                                'image': "img/ferns.png"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        'text': { 'name': "mosses and allies" },
                                                        'image': "img/mosses.png"
                                                    }
                                                ]
                                            },
                                            {
                                                'text': { 'name': "green algae" },
                                                'image': "img/greenalgae.png"
                                            }
                                        ]
                                    },
                                    {
                                        'pseudo': True,
                                        'children': [
                                            {
                                                'text': { 'name': "fungi and lichens" },
                                                'image': "img/fungi.png"
                                            },
                                            {
                                                'text': { 'name': "ANIMALS" },
                                                'HTMLclass': "the-parent",
                                                'children': [
                                                    {
                                                        'text': { 'name': "sponges" },
                                                        'image': "img/spuzva.png"
                                                    },
                                                    {
                                                        'pseudo': True,
                                                        'children': [
                                                            {
                                                                'text': { 'name': "cnidarians" },
                                                                'image': "img/cnidarians.png"
                                                            },
                                                            {
                                                                'pseudo': True,
                                                                'childrenDropLevel': 1,
                                                                'children': [
                                                                    {
                                                                        'pseudo': True,
                                                                        'children': [
                                                                            {
                                                                                'text': { 'name': "echinoderms" },
                                                                                'image': "img/zvezda.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "VERTEBRATES" },
                                                                                'HTMLclass': "the-parent",
                                                                                'children': [
                                                                                    {
                                                                                        'text': { 'name': "cartilaginous fish" },
                                                                                        'image': "img/cartilaginousfish.png"
                                                                                    },
                                                                                    {
                                                                                        'text': { 'name': "bony fish" },
                                                                                        'image': "img/bonyfish.png"
                                                                                    },
                                                                                    {
                                                                                        'text': { 'name': "TETRAPODS" },
                                                                                        'HTMLclass': "the-parent",
                                                                                        'children': [
                                                                                            {
                                                                                                'text': { 'name': "amphibians" },
                                                                                                'image': "img/zaba.png"
                                                                                            },
                                                                                            {
                                                                                                'text': { 'name': "AMNIOTES" },
                                                                                                'HTMLclass': "the-parent",
                                                                                                'children': [
                                                                                                    {
                                                                                                        'pseudo': True,
                                                                                                        'children': [
                                                                                                            {
                                                                                                                'text': { 'name': "turtles" },
                                                                                                                'image': "img/kornjaca.png"
                                                                                                            },
                                                                                                            {
                                                                                                                'pseudo': True,
                                                                                                                'children': [
                                                                                                                    {
                                                                                                                        'text': { 'name': "snakes and lizards" },
                                                                                                                        'image': "img/zmijurina.png"
                                                                                                                    },
                                                                                                                    {
                                                                                                                        'text': { 'name': "crocodiles and birds" },
                                                                                                                        'image': "img/ptica.png"
                                                                                                                    }
                                                                                                                ]
                                                                                                            }
                                                                                                        ]
                                                                                                    },
                                                                                                    {
                                                                                                        'text': { 'name': "mammals" },
                                                                                                        'image': "img/slon.png"
                                                                                                    }
                                                                                                ]
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        'text': { 'name': "ARTHROPODS" },                                                                      
                                                                        'HTMLclass': "the-parent",
                                                                        'children': [
                                                                            {
                                                                                'text': { 'name': "chelicerates" },
                                                                                'image': "img/chelirates.png"
                                                                            },
                                                                            {
                                                                                'pseudo': True,
                                                                                'stackchildren': True,
                                                                                'children': [
                                                                                    {
                                                                                        'text': { 'name': "crustaceans" },
                                                                                        'image': "img/rak.png"
                                                                                    },
                                                                                    {
                                                                                        'text': { 'name': "insects and myriapods" },
                                                                                        'image': "img/insekti.png"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        'pseudo': True,
                                                                        'children': [
                                                                            {
                                                                                'text': { 'name': "flatworms" },
                                                                                'image': "img/flatare.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "lophophorates" },
                                                                                'image': "img/lophoprates.png"
                                                                            }

                                                                        ]
                                                                    },
                                                                    {
                                                                        'pseudo': True,
                                                                        'childrenDropLevel': 1,
                                                                        'stackchildren': True,
                                                                        'children': [
                                                                            {
                                                                                'text': { 'name': "rotifers" },
                                                                                'image': "img/rotfiers.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "roundworms" },
                                                                                'image': "img/roundworms.png"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        'pseudo': True,
                                                                        'childrenDropLevel': 1,
                                                                        'stackchildren': True,
                                                                        'children': [
                                                                            {
                                                                                'text': { 'name': "mollusks" },
                                                                                'image': "img/mosculs.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "segmented worms" },
                                                                                'image': "img/segmentedworms.png"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pass

