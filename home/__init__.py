from home.models import call


def __init__(self, batch_size, num_patches, **kwargs):
        super(call, self).__init__()
        self.name = batch_size
        self.surname = num_patches