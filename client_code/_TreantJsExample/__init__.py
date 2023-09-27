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
                'image': "_/theme/img/truebacteria.png"
            },
            {
                'pseudo': True,
                'children': [
                    {
                        'text': { 'name': "archea bacteria" },
                        'image': "_/theme/img/archaebacteria.png"
                    },
                    {
                        'text': { 'name': "EUKARYOTES" },
                        'HTMLclass': "the-parent",
                        'children': [
                            {
                                'text': { 'name': "protocists" },
                                'image': "_/theme/img/protoctis.png"
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
                                                                        'image': "_/theme/img/cvijece2.png"
                                                                    },
                                                                    {
                                                                        'text': { 'name': "non-flowering seed plants" },
                                                                        'image': "_/theme/img/ne_cvijece.png"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                               'text': { 'name': "ferns and fern allies" },
                                                                'image': "_/theme/img/ferns.png"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        'text': { 'name': "mosses and allies" },
                                                        'image': "_/theme/img/mosses.png"
                                                    }
                                                ]
                                            },
                                            {
                                                'text': { 'name': "green algae" },
                                                'image': "_/theme/img/greenalgae.png"
                                            }
                                        ]
                                    },
                                    {
                                        'pseudo': True,
                                        'children': [
                                            {
                                                'text': { 'name': "fungi and lichens" },
                                                'image': "_/theme/img/fungi.png"
                                            },
                                            {
                                                'text': { 'name': "ANIMALS" },
                                                'HTMLclass': "the-parent",
                                                'children': [
                                                    {
                                                        'text': { 'name': "sponges" },
                                                        'image': "_/theme/img/spuzva.png"
                                                    },
                                                    {
                                                        'pseudo': True,
                                                        'children': [
                                                            {
                                                                'text': { 'name': "cnidarians" },
                                                                'image': "_/theme/img/cnidarians.png"
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
                                                                                'image': "_/theme/img/zvezda.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "VERTEBRATES" },
                                                                                'HTMLclass': "the-parent",
                                                                                'children': [
                                                                                    {
                                                                                        'text': { 'name': "cartilaginous fish" },
                                                                                        'image': "_/theme/img/cartilaginousfish.png"
                                                                                    },
                                                                                    {
                                                                                        'text': { 'name': "bony fish" },
                                                                                        'image': "_/theme/img/bonyfish.png"
                                                                                    },
                                                                                    {
                                                                                        'text': { 'name': "TETRAPODS" },
                                                                                        'HTMLclass': "the-parent",
                                                                                        'children': [
                                                                                            {
                                                                                                'text': { 'name': "amphibians" },
                                                                                                'image': "_/theme/img/zaba.png"
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
                                                                                                                'image': "_/theme/img/kornjaca.png"
                                                                                                            },
                                                                                                            {
                                                                                                                'pseudo': True,
                                                                                                                'children': [
                                                                                                                    {
                                                                                                                        'text': { 'name': "snakes and lizards" },
                                                                                                                        'image': "_/theme/img/zmijurina.png"
                                                                                                                    },
                                                                                                                    {
                                                                                                                        'text': { 'name': "crocodiles and birds" },
                                                                                                                        'image': "_/theme/img/ptica.png"
                                                                                                                    }
                                                                                                                ]
                                                                                                            }
                                                                                                        ]
                                                                                                    },
                                                                                                    {
                                                                                                        'text': { 'name': "mammals" },
                                                                                                        'image': "_/theme/img/slon.png"
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
                                                                                'image': "_/theme/img/chelirates.png"
                                                                            },
                                                                            {
                                                                                'pseudo': True,
                                                                                'stackchildren': True,
                                                                                'children': [
                                                                                    {
                                                                                        'text': { 'name': "crustaceans" },
                                                                                        'image': "_/theme/img/rak.png"
                                                                                    },
                                                                                    {
                                                                                        'text': { 'name': "insects and myriapods" },
                                                                                        'image': "_/theme/img/insekti.png"
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
                                                                                'image': "_/theme/img/flatare.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "lophophorates" },
                                                                                'image': "_/theme/img/lophoprates.png"
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
                                                                                'image': "_/theme/img/rotfiers.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "roundworms" },
                                                                                'image': "_/theme/img/roundworms.png"
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
                                                                                'image': "_/theme/img/mosculs.png"
                                                                            },
                                                                            {
                                                                                'text': { 'name': "segmented worms" },
                                                                                'image': "_/theme/img/segmentedworms.png"
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
    self.treant_js_1.node_structure = self.node

