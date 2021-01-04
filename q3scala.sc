class Solution {
    
    def getRecipient(message: String, position: Int): String = {
        util.Try("""@[-_a-zA-Z0-9]+""".r.findAllIn(message).toArray.apply(position-1).tail).getOrElse("")
    }

}
