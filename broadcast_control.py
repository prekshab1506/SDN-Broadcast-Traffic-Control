from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class BroadcastControl(object):

    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed

        # If packet is not parsed properly, ignore
        if not packet.parsed:
            return

        # Check if destination is broadcast
        if packet.dst.is_broadcast:
            log.info("Broadcast packet detected - DROPPED")
            return  # Drop packet (do nothing)

        # Otherwise, flood normally
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(msg)


def launch():
    def start_switch(event):
        log.info("Controlling %s" % (event.connection,))
        BroadcastControl(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
