"""重垠（CHONGYIN）· 异地灾备副本

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：异地灾备副本。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Chongyin:
    """重垠（CHONGYIN）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "CHONGYIN"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.replicas = {}
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "chongyin",
            "cn": "重垠",
            "code": self.CODE,
            "duty": "异地灾备副本",
            "mingwen": "重垠设守，正本不毁",
            "anchor": self.ANCHOR,
        }

    def replicate(self, artifact):
        """副本设守异地，返回副本址。"""
        import hashlib, json
        payload = json.dumps(artifact, sort_keys=True, ensure_ascii=False)
        self._seq += 1
        rid = "CY-%04d" % self._seq
        self.replicas[rid] = {"replica_id": rid, "content": artifact,
                              "hash": hashlib.sha256(payload.encode()).hexdigest()}
        self.events.append({"event": "replicate", "replica_id": rid})
        return rid

    def verify_replica(self, replica_id):
        """核验副本与正本一致。"""
        import hashlib, json
        if replica_id not in self.replicas:
            raise KeyError("无此副本： %s" % replica_id)
        rep = self.replicas[replica_id]
        payload = json.dumps(rep["content"], sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(payload.encode()).hexdigest() == rep["hash"]
