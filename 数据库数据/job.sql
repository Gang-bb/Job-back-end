/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : job

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 28/08/2020 17:30:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('a86919c9c621');

-- ----------------------------
-- Table structure for com_sign
-- ----------------------------
DROP TABLE IF EXISTS `com_sign`;
CREATE TABLE `com_sign`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `uId` bigint(20) NULL DEFAULT NULL COMMENT '关联的公司用户id',
  `cId` bigint(20) NULL DEFAULT NULL COMMENT '关联的公司id',
  `isVerify` smallint(6) NULL DEFAULT NULL COMMENT '是否通过审核 1-提交待审核 2-通过 3-不通过',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '309 公司信息提交审核记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of com_sign
-- ----------------------------
INSERT INTO `com_sign` VALUES (4, 0, 1587609344, 1587618367, 0, 0, 5, 3, 2);
INSERT INTO `com_sign` VALUES (5, 0, 1587626913, 1587626913, 0, 0, 3, 2, 1);

-- ----------------------------
-- Table structure for com_sign2
-- ----------------------------
DROP TABLE IF EXISTS `com_sign2`;
CREATE TABLE `com_sign2`  (
  `id` bigint(20) NOT NULL COMMENT '主键id',
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名字',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '309 公司信息提交审核记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of com_sign2
-- ----------------------------
INSERT INTO `com_sign2` VALUES (1011258277019817480, '000');
INSERT INTO `com_sign2` VALUES (1011258277020186578, '000');
INSERT INTO `com_sign2` VALUES (1011258277020207550, '000');

-- ----------------------------
-- Table structure for company
-- ----------------------------
DROP TABLE IF EXISTS `company`;
CREATE TABLE `company`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `cname` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '公司的名字',
  `uId` bigint(20) NULL DEFAULT NULL COMMENT '关联的用户id',
  `cemail` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '企业邮箱',
  `cinfo` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '简介',
  `cphone` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '企业电话',
  `cplace` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在城市',
  `ctype` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属行业',
  `pname` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '联系人姓名',
  `pphone` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '联系人手机号',
  `isVerify` smallint(6) NULL DEFAULT NULL COMMENT '是否通过审核 1-待审核 2-通过 3-未通过',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '307 公司信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of company
-- ----------------------------
INSERT INTO `company` VALUES (2, 0, 1587288340, 1587619968, 0, 0, '中国移动-广西总公司', 3, 'gang_bb@163.com', '中国电信集团有限公司（简称“中国电信”）是国有特大型通信骨干企业，注册资本2131亿元人民币，资产规模超过8000亿元人民币，年收入规模超过4300亿元人民币，连续多年位列《财富》杂志全球500强。', '0771-5584523', '南宁青秀区广西壮族自治区建信路1号金湖广场', 'IT/互联网/网络', '张三', '18276669982', 2);
INSERT INTO `company` VALUES (3, 0, 1587609344, 1587618367, 0, 0, '广西民族大学', 5, '949526365@qq.com', '我是一个学校哦', '13978229191', '民大', '学校', '梁艺翔', '12123123123', 2);

-- ----------------------------
-- Table structure for job
-- ----------------------------
DROP TABLE IF EXISTS `job`;
CREATE TABLE `job`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `tittle` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '工作的标题',
  `reward` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '报酬',
  `place` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '地点',
  `settlement` smallint(6) NOT NULL COMMENT '工作结算方式 1-日结 2-周结 3-完工结',
  `isBagEating` smallint(6) NOT NULL COMMENT '是否包吃 1-是 2-否',
  `encase` smallint(6) NOT NULL COMMENT '是否包住 1-是 2-否',
  `isTrafficSubsidy` smallint(6) NOT NULL COMMENT '是否有交通补贴 1-是 2-否',
  `royalty` smallint(6) NOT NULL COMMENT '是否有提成 1-是 2-否',
  `browseTimes` int(11) NULL DEFAULT NULL COMMENT '浏览次数',
  `content` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '工作内容',
  `detailPlace` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '详细地址',
  `endTime` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '结束时间',
  `fromCompany` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '发布的企业',
  `recruitNum` int(11) NULL DEFAULT NULL COMMENT '招聘人数',
  `sex` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别要求 1-男 2-女 3-男女不限',
  `startTime` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '开始时间',
  `type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '工作类型',
  `withPeople` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '企业联系人',
  `signNum` int(11) NULL DEFAULT NULL COMMENT '当前报名人数人数',
  `cId` bigint(20) NULL DEFAULT NULL COMMENT '企业的id号',
  `email` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '企业联系人邮箱',
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '企业联系人电话',
  `status` smallint(6) NULL DEFAULT NULL COMMENT '当前状态 1-待审批 2-进行中 3-已结束',
  `testUnique` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '测试是否唯一',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `testUnique`(`testUnique`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 68 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '300 工作表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of job
-- ----------------------------
INSERT INTO `job` VALUES (30, 0, 1587626913, 1588772079, 0, 0, '989898', '10元/日结', '西乡塘', 1, 2, 2, 1, 1, 100, '1、派发前发单员应基本了解当次所派发DM单页的产品特性和服务内容，确定所宣百传产品的主题，锁定目标客户群，提高派发效率.\n2、派发的时间要集中在上下班的高峰期，派发地点应选在目标客户群比较集中的地点（如通往写字楼的主要路口，地铁口）。\n3、发单过程中始终保持友善、热情、微笑的面孔，让度人容易接近，进而有兴趣了解所派发的DM宣传单，并引起问客户群对产品的好奇和好感。\n4、发传单要在行人过往的路线上，最好不要挡在行人的面前（一定要准备好，不要突然举起你的手）；在答卖场出入口发单时，身子侧站，不要挡住顾客的路。发单时，尽量往行人有空闲的手上递！\n5、拿宣传单动作，建议以一边的手臂为依托托着宣传单，宣传单正面朝向行人，将客户产品或服务的内容展现出来，确保行人拿到的宣传单是正的，以便行人比较方便的第一时间看到上版面的内容。\n6、发单时要有针对性地派发，切忌不加选择的随意乱派发。\n7、发单时要用礼貌的语言与消费者沟通，一定不能害羞，大胆的说出产品的主题，权（最好总结在10个字以内）而不是简单的发单机器人.\n8、发单时要善于观察，及时走动派发，要主动。', '西乡塘市场门口', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '派单', '小韦', 1, 2, '949526365@qq.com', '13978223101', 2, NULL);
INSERT INTO `job` VALUES (31, 0, 1587626913, 1588772079, 0, 0, '酷乐乐转单派送员', '100元/完工结', '西乡塘', 3, 1, 1, 2, 2, 100, '负责每日的餐具清洗！负责每日的餐具清洗！负责每日的餐具清洗！', '西乡塘大酒店', '2020-08-23', '中国移动-广西总公司', 2, '3', '2020-04-23', '服务员', '小梁', 0, 2, '949526365@qq.com', '13978220181', 2, NULL);
INSERT INTO `job` VALUES (32, 0, 1588580001, 1588772079, 0, 1, '2222299911', '4566元/周结', '西乡塘', 2, 2, 1, 2, 2, 100, '2342324241·3232323233', '324324242423424', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '派单', '23刚刚', 0, 2, '32131233123', '给他个人', 2, NULL);
INSERT INTO `job` VALUES (33, 0, 1588580001, 1588684776, 0, 0, '市场水果搬运工', '233元/日结', '西乡塘', 1, 2, 2, 2, 2, 100, '4444444444444444444444444444444444', '31', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '客服', '·13·3', 0, 2, '1423435353', '·31·3', 2, NULL);
INSERT INTO `job` VALUES (34, 0, 1588580001, 1588683982, 0, 0, '网吧游戏策划运营', '343元/日结', '西乡塘', 1, 1, 2, 2, 2, 100, '453533333333333333333333333333333333333333', '45645 4好他人人', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '促销', '34', 0, 2, '2··13·3', '4341', 2, NULL);
INSERT INTO `job` VALUES (35, 0, 1588580001, 1588580001, 0, 0, '婚礼活动执行', '231元/日结', '西乡塘', 1, 1, 1, 2, 1, 100, '66666666666666666666666666666666666666666', '23424324242', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '网络编辑', '1232131', 0, 2, '31312321212', '123123', 2, NULL);
INSERT INTO `job` VALUES (36, 0, 1588580001, 1588685637, 0, 0, '空调安装工', '456元/完工结', '西乡塘', 3, 1, 1, 1, 1, 100, '123131231312222222222222222222222222222', '12312321313213131313', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '调研', '2131223131', 0, 2, '1232131', '123213123', 2, NULL);
INSERT INTO `job` VALUES (38, 0, 1588649229, 1588685637, 0, 1, '65555555555555555', '234234234元/周结', '西乡塘', 2, 2, 2, 2, 2, 100, '65555555555555555555555555555555555', '56565', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '客服', '424', 0, 2, 'j嘤嘤嘤', '56', 1, NULL);
INSERT INTO `job` VALUES (54, 0, 1588770886, 1588770886, 0, 0, '99911', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (55, 0, 1588770958, 1588770958, 0, 0, '99911', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (56, 0, 1588771028, 1588771028, 0, 0, '99911', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (57, 0, 1588771028, 1588771028, 0, 0, '99911', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (58, 0, 1588771028, 1588771028, 0, 0, '99', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (59, 0, 1588771028, 1588771028, 0, 0, '11', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (60, 0, 1588771028, 1588771028, 0, 0, '11', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (61, 0, 1588771776, 1588771776, 0, 0, '2222299911', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (62, 0, 1588771776, 1588771776, 0, 0, '2222299911', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (63, 0, 1588771776, 1588771776, 0, 0, '11', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (64, 0, 1588771776, 1588771776, 0, 0, '11', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (65, 0, 1588771776, 1588771776, 0, 0, '2222299911', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (66, 0, 1588771776, 1588771776, 0, 0, '343434', NULL, NULL, 3, 2, 2, 2, 2, 100, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 1, NULL);
INSERT INTO `job` VALUES (67, 0, 1598600546, 1598600546, 0, 0, '1', '12元/日结', '西乡塘', 1, 2, 2, 2, 2, 100, '255555555555555555555555555555555555555555555555555555555555555555555', '12', '2020-04-23', '中国移动-广西总公司', 1, '3', '2020-04-23', '调研', '1212', 0, 2, '212', '12121', 1, NULL);

-- ----------------------------
-- Table structure for job_signup
-- ----------------------------
DROP TABLE IF EXISTS `job_signup`;
CREATE TABLE `job_signup`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `jobId` bigint(20) NULL DEFAULT NULL COMMENT '申请工作的id号',
  `message` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生给企业的留言',
  `userId` bigint(20) NULL DEFAULT NULL COMMENT '申请学生的用户id号',
  `status` smallint(6) NULL DEFAULT NULL COMMENT '状态 1-已报名 2-已录用 3-已到岗 4-已结算',
  `stuId` bigint(20) NULL DEFAULT NULL COMMENT '申请学生的学生id号',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '302 提交工作记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of job_signup
-- ----------------------------
INSERT INTO `job_signup` VALUES (14, 0, 1587626913, 1587626913, 0, 0, 30, '未读的无多', 4, 2, 1);

-- ----------------------------
-- Table structure for resume_edu
-- ----------------------------
DROP TABLE IF EXISTS `resume_edu`;
CREATE TABLE `resume_edu`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `userId` bigint(20) NULL DEFAULT NULL COMMENT '关联userId号',
  `school` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学校',
  `major` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '专业',
  `degree` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学历',
  `startTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '开始时间',
  `endTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '结束时间',
  `experience` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '在校经历',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '304 教育经历表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of resume_edu
-- ----------------------------
INSERT INTO `resume_edu` VALUES (1, 0, 1586938446, 1587457237, 0, 0, 4, '广西民族大学', '软件工程', '本科', '2016-09', '2020-06', '我在学校表现得很好很好哦');

-- ----------------------------
-- Table structure for resume_other
-- ----------------------------
DROP TABLE IF EXISTS `resume_other`;
CREATE TABLE `resume_other`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `userId` bigint(20) NULL DEFAULT NULL COMMENT '关联userId号',
  `expectedJobType` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '期望工作类型',
  `shortJobTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '短期工作时间',
  `ableWorkDay` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '可上班时间',
  `selfIntroduction` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '自我介绍',
  `isFullTime` smallint(6) NULL DEFAULT NULL COMMENT '是否支持全职上班 1-是 0-否',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '306 简历其他项' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of resume_other
-- ----------------------------
INSERT INTO `resume_other` VALUES (1, 0, 1586951834, 1587624610, 0, 0, 4, '周末兼职', '周末', '每周一天', '', 1);

-- ----------------------------
-- Table structure for resume_work
-- ----------------------------
DROP TABLE IF EXISTS `resume_work`;
CREATE TABLE `resume_work`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `userId` bigint(20) NULL DEFAULT NULL COMMENT '关联userId号',
  `company` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '公司名',
  `startTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '开始时间',
  `endTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '结束时间',
  `experience` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '在职经历',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '306 工作经历表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of resume_work
-- ----------------------------
INSERT INTO `resume_work` VALUES (3, 0, 1587624610, 1587624610, 0, 0, 4, '阿里巴巴', '2018-04-23', '2019-04-23', '我在期间干过软件开发');

-- ----------------------------
-- Table structure for search
-- ----------------------------
DROP TABLE IF EXISTS `search`;
CREATE TABLE `search`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `message` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '搜索的信息',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '303 热门搜索表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of search
-- ----------------------------
INSERT INTO `search` VALUES (1, NULL, NULL, NULL, NULL, 0, '日结');
INSERT INTO `search` VALUES (2, NULL, NULL, NULL, NULL, 0, '在家兼职');
INSERT INTO `search` VALUES (3, NULL, NULL, NULL, NULL, 0, '发传单');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `sname` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生的名字',
  `uId` bigint(20) NULL DEFAULT NULL COMMENT '关联的用户id',
  `age` int(11) NULL DEFAULT NULL COMMENT '用户的年龄',
  `bestEdu` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '最高学历',
  `birthday` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '生日',
  `eduStatus` smallint(6) NULL DEFAULT NULL COMMENT '教育状态 1-在读 2-已毕业',
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `height` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '身高',
  `nativePlace` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在城市',
  `phoneNumber` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `place` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在地级市',
  `qqNum` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'QQ',
  `weChat` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '微信号',
  `sex` smallint(6) NULL DEFAULT NULL COMMENT '性别 1-男 2-女',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '308 学生信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, NULL, NULL, 1587514466, NULL, 0, '梁艺翔', 4, 23, '本科', '1998-03-15', 1, '949526365@qq.com', '170', NULL, '13978223101', '南宁', '949526365', '', 1);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creator` bigint(20) NULL DEFAULT NULL COMMENT '创建人',
  `creatTime` int(11) NULL DEFAULT NULL COMMENT '创建时间',
  `reviseTime` int(11) NULL DEFAULT NULL COMMENT '更新时间',
  `reviser` bigint(20) NULL DEFAULT NULL COMMENT '修改人',
  `isDel` smallint(6) NULL DEFAULT NULL COMMENT '是否删除 1-删除 0-未删除',
  `loginName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登录名',
  `password` varchar(210) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登录密码',
  `type` smallint(6) NULL DEFAULT NULL COMMENT '身份类型 1-系统管理员 2-企业 3-学生',
  `openId` varchar(300) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '微信小程序用户唯一标识id',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `loginName`(`loginName`) USING BTREE,
  UNIQUE INDEX `openId`(`openId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '305 用户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (3, 0, 1587276197, 1587350655, 0, 0, 'c', 'pbkdf2:sha256:150000$uSdqWJXz$d727fe2e33966eeb3b562572b6b075029efeecef1c378aa33315843c30f5b6c5', 2, NULL);
INSERT INTO `user` VALUES (4, 0, 1587354407, 1587354407, 0, 0, NULL, NULL, 3, 'obbTU5DjnMdRlQQsRdByH66V441s');

SET FOREIGN_KEY_CHECKS = 1;
