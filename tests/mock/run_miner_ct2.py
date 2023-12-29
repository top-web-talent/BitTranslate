from neurons.miners.m2m_ctranslate2_miner import CT2M2MMiner
from mock.mock_network import mocked_network
import time
from neurons.protocol import Translate

def main():
    with mocked_network():
        miner = CT2M2MMiner()

    miner.axon.start()

    synapse = Translate(
                source_texts=["hello world"],
                source_lang="en",
                target_lang="pl"
            )

    print("Result: ", miner.forward(synapse))



if __name__ == "__main__":
    main()
